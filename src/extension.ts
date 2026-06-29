import * as vscode from "vscode";

const PSJ_DOC_BASE = "https://psjdoc.e-technostar.com/";

/**
 * Builds the documentation URL for a PSJ function reference.
 *
 * - JPT utilities (e.g. `JPT.Foo`) live under `docs/psj-utility/`.
 * - PSJ commands live under `docs/psj-command/<kebab-category>/<FnName>`.
 */
function buildReferenceLink(fnName: string): string {
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

const hoverProvider: vscode.HoverProvider = {
  provideHover(document, position) {
    const wordRange = document.getWordRangeAtPosition(position);
    const word = document.getText(wordRange);
    const linePrefix = document.lineAt(position).text;
    const fnNameMatch = linePrefix.match(/^.*(?=\()/);
    const prefixMatch = linePrefix.match(/(?<=\.)\w*(?=\()/);

    if (fnNameMatch === null || prefixMatch === null || prefixMatch[0] !== word) {
      return undefined;
    }

    const fnNameParts = fnNameMatch[0].split("=");
    const rawFnName = fnNameParts[fnNameParts.length - 1];
    if (rawFnName === undefined) {
      return undefined;
    }

    const fnName = rawFnName.trim();
    const markdown = new vscode.MarkdownString();
    markdown.appendMarkdown(`[See reference here](${buildReferenceLink(fnName)})`);

    return new vscode.Hover(markdown);
  },
};

export function activate(context: vscode.ExtensionContext): void {
  context.subscriptions.push(
    vscode.languages.registerHoverProvider("python", hoverProvider),
  );
}

export function deactivate(): void {
  // Nothing to clean up.
}
