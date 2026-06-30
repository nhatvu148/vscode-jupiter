import * as vscode from "vscode";
import { allApiEntries, allKeywords, lookupApi } from "./jupiterApi";

const LANGUAGES = ["python", "jupiter"];

/** Extracts the fully-qualified function name being called on the hovered line. */
function functionNameAt(
  document: vscode.TextDocument,
  position: vscode.Position,
): string | undefined {
  const word = document.getText(document.getWordRangeAtPosition(position));
  const linePrefix = document.lineAt(position).text;
  const fnNameMatch = linePrefix.match(/^.*(?=\()/);
  const prefixMatch = linePrefix.match(/(?<=\.)\w*(?=\()/);

  if (fnNameMatch === null || prefixMatch === null || prefixMatch[0] !== word) {
    return undefined;
  }

  const fnNameParts = fnNameMatch[0].split("=");
  const rawFnName = fnNameParts[fnNameParts.length - 1];
  return rawFnName === undefined ? undefined : rawFnName.trim();
}

const hoverProvider: vscode.HoverProvider = {
  provideHover(document, position) {
    const fnName = functionNameAt(document, position);
    if (fnName === undefined) {
      return undefined;
    }

    const api = lookupApi(fnName);
    if (!api) {
      return undefined;
    }

    return new vscode.Hover(new vscode.MarkdownString(api.doc));
  },
};

/** Pre-built completion items for every known PSJ/JPT API entry. */
const apiCompletionItems: vscode.CompletionItem[] = allApiEntries().map(
  (entry) => {
    const item = new vscode.CompletionItem(
      entry.prefix,
      vscode.CompletionItemKind.Method,
    );
    item.detail = entry.name;
    item.documentation = new vscode.MarkdownString(entry.doc);
    return item;
  },
);

/** PSJ utility constants + GUI keywords, ranked below the documented methods. */
const keywordCompletionItems: vscode.CompletionItem[] = allKeywords().map(
  (keyword) => {
    const item = new vscode.CompletionItem(
      keyword.label,
      vscode.CompletionItemKind.Constant,
    );
    item.detail = `Jupiter ${keyword.group}`;
    item.sortText = `zz${keyword.label}`;
    return item;
  },
);

const allCompletionItems = [...apiCompletionItems, ...keywordCompletionItems];

const completionProvider: vscode.CompletionItemProvider = {
  provideCompletionItems() {
    return allCompletionItems;
  },
};

/**
 * Finds the call the cursor is inside: walks back to the unmatched "(" and
 * returns the function name before it and how many top-level commas precede
 * the cursor (the active parameter index).
 */
export function findEnclosingCall(
  text: string,
): { name: string; activeParam: number } | undefined {
  let depth = 0;
  for (let i = text.length - 1; i >= 0; i--) {
    const ch = text[i];
    if (ch === ")" || ch === "]" || ch === "}") {
      depth++;
    } else if (ch === "(" || ch === "[" || ch === "{") {
      if (depth > 0) {
        depth--;
        continue;
      }
      if (ch !== "(") {
        return undefined;
      }
      const name = text.slice(0, i).match(/([A-Za-z_][A-Za-z0-9_.]*)$/);
      if (!name) {
        return undefined;
      }
      let argDepth = 0;
      let commas = 0;
      for (const c of text.slice(i + 1)) {
        if ("([{".includes(c)) {
          argDepth++;
        } else if (")]}".includes(c)) {
          argDepth--;
        } else if (c === "," && argDepth === 0) {
          commas++;
        }
      }
      return { name: name[1], activeParam: commas };
    }
  }
  return undefined;
}

const signatureProvider: vscode.SignatureHelpProvider = {
  provideSignatureHelp(document, position) {
    const prefix = document
      .lineAt(position.line)
      .text.slice(0, position.character);
    const call = findEnclosingCall(prefix);
    if (!call) {
      return undefined;
    }

    const api = lookupApi(call.name);
    if (!api || api.params.length === 0) {
      return undefined;
    }

    const info = new vscode.SignatureInformation(
      api.signature,
      new vscode.MarkdownString(api.doc),
    );
    info.parameters = api.params.map((p) => new vscode.ParameterInformation(p));

    const help = new vscode.SignatureHelp();
    help.signatures = [info];
    help.activeSignature = 0;
    help.activeParameter = Math.min(call.activeParam, api.params.length - 1);
    return help;
  },
};

export function activate(context: vscode.ExtensionContext): void {
  for (const language of LANGUAGES) {
    context.subscriptions.push(
      vscode.languages.registerHoverProvider(language, hoverProvider),
      vscode.languages.registerCompletionItemProvider(
        language,
        completionProvider,
      ),
      vscode.languages.registerSignatureHelpProvider(
        language,
        signatureProvider,
        "(",
        ",",
      ),
    );
  }
}

export function deactivate(): void {
  // Nothing to clean up.
}
