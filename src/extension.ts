import * as vscode from "vscode";
import path = require("path");
import {
  root1,
  root2,
  root3,
  root4,
  map12,
  map23,
  map34,
  map45,
  libKey,
  psjUtilKeys,
  psjGuiKeys,
  callTips,
} from "./data";
import Document from "./document";

export function activate(context: vscode.ExtensionContext) {
  const definition = vscode.languages.registerDefinitionProvider("python", {
    provideDefinition(
      document: vscode.TextDocument,
      position: vscode.Position,
      token: vscode.CancellationToken,
    ) {
      const wordRange = document.getWordRangeAtPosition(position);
      const word = document.getText(wordRange);
      const linePrefix = document.lineAt(position).text;
      const fnName = linePrefix.match(/^.*(?=\()/);

      // @ts-ignore
      if (fnName !== null && callTips[fnName[0]].prefix === word) {
        return new vscode.Location(
          // vscode.Uri.file(`${path.dirname(document.fileName)}/out/Analysis/__init__.pyi`),
          vscode.Uri.file(
            `C:/Program Files/TechnoStar/Jupiter-Pre_5.0/macro/Analysis/AbaqusStep.py`,
          ),
          new vscode.Position(4, 1),
        );
      } else {
        return undefined;
      }
    },
  });

  const document = vscode.commands.registerCommand(
    "extension.gotoDocument",
    (e: vscode.Uri) => {
      let editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showWarningMessage("No active text editor found!");
        return;
      }

      let keyword: string = "";
      if (editor.selection.isEmpty) {
        let wordRange: any = editor.document.getWordRangeAtPosition(
          editor.selection.start,
        );
        keyword = wordRange ? editor.document.getText(wordRange) : "";
      } else {
        keyword = editor.document.getText(editor.selection.with());
      }
      let extIndex: number = editor.document.fileName.lastIndexOf(".");
      let ext: string =
        extIndex >= 0 ? editor.document.fileName.substring(extIndex + 1) : "";
      let config = vscode.workspace.getConfiguration("goto-documentation");
      let customDocs = config.get<object>("customDocs");

      Document.open(ext, keyword, customDocs);
    },
  );

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

  const keywords = vscode.languages.registerCompletionItemProvider("python", {
    provideCompletionItems(
      document: vscode.TextDocument,
      position: vscode.Position,
      token: vscode.CancellationToken,
    ) {
      const libKeyList = libKey.map((a) => new vscode.CompletionItem(a.trim()));
      const psjUtilKeyList = psjUtilKeys.map(
        (a) => new vscode.CompletionItem(a.trim()),
      );
      const psjGuiKeyList = psjGuiKeys.map(
        (a) => new vscode.CompletionItem(a.trim()),
      );
      return [...libKeyList, ...psjUtilKeyList, ...psjGuiKeyList];
    },
  });

  root1.forEach((el: string) => {
    context.subscriptions.push(
      vscode.languages.registerCompletionItemProvider("python", {
        provideCompletionItems(
          document: vscode.TextDocument,
          position: vscode.Position,
          token: vscode.CancellationToken,
        ) {
          return [new vscode.CompletionItem(el)];
        },
      }),
    );
  });

  root1.forEach((el: string) => {
    vscode.languages.registerCompletionItemProvider(
      "python",
      {
        provideCompletionItems(
          document: vscode.TextDocument,
          position: vscode.Position,
        ) {
          const linePrefix = document
            .lineAt(position)
            .text.substr(0, position.character);
          if (!linePrefix.endsWith(el + ".")) {
            return undefined;
          }

          // @ts-ignore
          return map12[el].map(
            (element: string) =>
              new vscode.CompletionItem(
                element,
                vscode.CompletionItemKind.Method,
              ),
          );
        },
      },
      ".",
    );
  });

  root2.forEach((el: string) => {
    vscode.languages.registerCompletionItemProvider(
      "python",
      {
        provideCompletionItems(
          document: vscode.TextDocument,
          position: vscode.Position,
        ) {
          const linePrefix = document
            .lineAt(position)
            .text.substr(0, position.character);
          // @ts-ignore
          const prefix = root1.find((a: string) => map12[a].includes(el));

          if (!linePrefix.endsWith(prefix + "." + el + ".")) {
            return undefined;
          }

          // @ts-ignore
          return map23[el]
            .filter((a: string | null) => a !== null)
            .map(
              (element: string) =>
                new vscode.CompletionItem(
                  element,
                  vscode.CompletionItemKind.Method,
                ),
            );
        },
      },
      ".",
    );
  });

  root3.forEach((el: string) => {
    vscode.languages.registerCompletionItemProvider(
      "python",
      {
        provideCompletionItems(
          document: vscode.TextDocument,
          position: vscode.Position,
        ) {
          const linePrefix = document
            .lineAt(position)
            .text.substr(0, position.character);
          // @ts-ignore
          const prefix = root2.find((a: string) => map23[a].includes(el));
          const prePrefix = root1.find((a: string) =>
            // @ts-ignore
            map12[a].includes(prefix),
          );

          if (!linePrefix.endsWith(prePrefix + "." + prefix + "." + el + ".")) {
            return undefined;
          }

          // @ts-ignore
          return map34[el]
            .filter((a: string | null) => a !== null)
            .map(
              (element: string) =>
                new vscode.CompletionItem(
                  element,
                  vscode.CompletionItemKind.Method,
                ),
            );
        },
      },
      ".",
    );
  });

  root4.forEach((el: string) => {
    vscode.languages.registerCompletionItemProvider(
      "python",
      {
        provideCompletionItems(
          document: vscode.TextDocument,
          position: vscode.Position,
        ) {
          const linePrefix = document
            .lineAt(position)
            .text.substr(0, position.character);
          // @ts-ignore
          const prefix = root3.find((a: string) => map34[a].includes(el));
          const prePrefix = root2.find((a: string) =>
            // @ts-ignore
            map23[a].includes(prefix),
          );
          const prePrePrefix = root1.find((a: string) =>
            // @ts-ignore
            map12[a].includes(prePrefix),
          );

          if (
            !linePrefix.endsWith(
              prePrePrefix + "." + prePrefix + "." + prefix + "." + el + ".",
            )
          ) {
            return undefined;
          }

          // @ts-ignore
          return map45[el]
            .filter((a: string | null) => a !== null)
            .map(
              (element: string) =>
                new vscode.CompletionItem(
                  element,
                  vscode.CompletionItemKind.Method,
                ),
            );
        },
      },
      ".",
    );
  });

  context.subscriptions.push(keywords, hover, document, definition);
}

export function deactivate() {}
