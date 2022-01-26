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

export function activate(context: vscode.ExtensionContext) {
  initBinary();
  handleSelection(context);

  const hover = vscode.languages.registerHoverProvider("python", {
    provideHover(document, position, token) {
      // const wordRange = document.getWordRangeAtPosition(position);
      // const word = document.getText(wordRange);
      const linePrefix = document.lineAt(position).text;
      const fnName0 = linePrefix.match(/^.*(?=\()/);

      if (fnName0 !== null) {
        const fnNameArr = fnName0[0].split("=");
        const fnName1 = fnNameArr[fnNameArr.length - 1];

        if (fnName1 !== undefined) {
          const fnName = fnName1.trim();
          const mdStr = new vscode.MarkdownString();

          let link = "https://psjdoc.e-technostar.com/";
          if (fnName.includes("JPT.")) {
            link = link + "docs/psj-utility/JPT." + fnName.split(".")[1];
          } else {
            link =
              link +
              "docs/psj-command/" +
              fnName
                .split(".")[0]
                .split(/(?=[A-Z][a-z])/)
                .map((s: string) => s.toLowerCase())
                .join("-") +
              "/" +
              fnName;
          }
          mdStr.appendMarkdown(`[See reference here](${link})`);

          return new vscode.Hover(mdStr);
        }
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
    ...COMPLETION_TRIGGERS,
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
      selectionHandler,
    ),
  );
}
