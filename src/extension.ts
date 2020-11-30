import * as vscode from "vscode";
import {
  deactivate as requestDeactivate,
  initBinary,
} from "./binary/requests/requests";
import { COMPLETION_IMPORTS, selectionHandler } from "./selectionHandler";
import {
  Capability,
  fetchCapabilitiesOnFocus,
  isCapabilityEnabled,
} from "./capabilities";
import provideCompletionItems from "./provideCompletionItems";
import { COMPLETION_TRIGGERS } from "./consts";
import handleErrorState from "./binary/errorState";
import {
  callTips,
} from "./data";

export function activate(context: vscode.ExtensionContext) {
  initBinary();
  handleSelection(context);

  const hover = vscode.languages.registerHoverProvider("python", {
    provideHover(document, position, token) {
      const wordRange = document.getWordRangeAtPosition(position);
      const word = document.getText(wordRange);
      const linePrefix = document.lineAt(position).text;
      const fnName = linePrefix.match(/^.*(?=\()/);

      // @ts-ignore
      if (fnName !== null && callTips[fnName[0]].prefix === word) {
        const mdStr = new vscode.MarkdownString();
        mdStr.appendCodeblock("(method) " + fnName[0], "javascript");
        mdStr.appendMarkdown("***  \n");
        // @ts-ignore
        mdStr.appendMarkdown(callTips[fnName[0]].text);
        mdStr.appendMarkdown("***  \n");
        mdStr.appendMarkdown(
          "[See reference here](https://psjdoc.e-technostar.com/)",
        );

        return new vscode.Hover(mdStr);
      } else {
        return undefined;
      }
    },
  });

  context.subscriptions.push(hover);

  void backgroundInit(context);
  return Promise.resolve();
}

async function backgroundInit(context: vscode.ExtensionContext) {
  // Goes to the binary to fetch what capabilities enabled:
  await fetchCapabilitiesOnFocus();

  vscode.languages.registerCompletionItemProvider(
    { pattern: "**" },
    {
      provideCompletionItems,
    },
    ...COMPLETION_TRIGGERS
  );

  if (isCapabilityEnabled(Capability.ON_BOARDING_CAPABILITY)) {
    handleErrorState();
  }
}

export async function deactivate(): Promise<unknown> {
  return requestDeactivate();
}

function handleSelection(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerTextEditorCommand(
      COMPLETION_IMPORTS,
      selectionHandler
    )
  );
}