import * as vscode from "vscode";
import { allApiEntries, lookupApi } from "./jupiterApi";

const PSJ_DOC_BASE = "https://psjdoc.e-technostar.com/";
const LANGUAGES = ["python", "jupiter"];

/**
 * Builds the documentation URL for a PSJ function reference.
 *
 * - JPT utilities (e.g. `JPT.Foo`) live under `docs/psj-utility/`.
 * - PSJ commands live under `docs/psj-command/<kebab-category>/<FnName>`.
 */
export function buildReferenceLink(fnName: string): string {
  if (fnName.includes("JPT.")) {
    return `${PSJ_DOC_BASE}docs/psj-utility/JPT.${fnName.split(".")[1]}`;
  }

  const category = fnName
    .split(".")[0]
    .split(/(?=[A-Z][a-z])/)
    .map((segment) => segment.toLowerCase())
    .join("-");

  return `${PSJ_DOC_BASE}docs/psj-command/${category}/${fnName}`;
}

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

    const markdown = new vscode.MarkdownString();
    const api = lookupApi(fnName);
    if (api) {
      markdown.appendMarkdown(`${api.doc}\n\n`);
    }
    markdown.appendMarkdown(`[See reference here](${buildReferenceLink(fnName)})`);

    return new vscode.Hover(markdown);
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

const completionProvider: vscode.CompletionItemProvider = {
  provideCompletionItems() {
    return apiCompletionItems;
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
    );
  }
}

export function deactivate(): void {
  // Nothing to clean up.
}
