import * as vscode from "vscode";
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

export function activate(context: vscode.ExtensionContext) {
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

  // root1.forEach((el: string) => {
  //   vscode.languages.registerCompletionItemProvider(
  //     "python",
  //     {
  //       provideCompletionItems(
  //         document: vscode.TextDocument,
  //         position: vscode.Position,
  //       ) {
  //         const linePrefix = document
  //           .lineAt(position)
  //           .text.substr(0, position.character);
  //         if (!linePrefix.endsWith(el + ".")) {
  //           return undefined;
  //         }

  //         // @ts-ignore
  //         return map12[el].map(
  //           (element: string) =>
  //             new vscode.CompletionItem(
  //               element,
  //               vscode.CompletionItemKind.Method,
  //             ),
  //         );
  //       },
  //     },
  //     ".",
  //   );
  // });

  // root2.forEach((el: string) => {
  //   vscode.languages.registerCompletionItemProvider(
  //     "python",
  //     {
  //       provideCompletionItems(
  //         document: vscode.TextDocument,
  //         position: vscode.Position,
  //       ) {
  //         const linePrefix = document
  //           .lineAt(position)
  //           .text.substr(0, position.character);
  //         // @ts-ignore
  //         const prefix = root1.find((a: string) => map12[a].includes(el));

  //         if (!linePrefix.endsWith(prefix + "." + el + ".")) {
  //           return undefined;
  //         }

  //         // @ts-ignore
  //         return map23[el]
  //           .filter((a: string | null) => a !== null)
  //           .map(
  //             (element: string) =>
  //               new vscode.CompletionItem(
  //                 element,
  //                 vscode.CompletionItemKind.Method,
  //               ),
  //           );
  //       },
  //     },
  //     ".",
  //   );
  // });

  // root3.forEach((el: string) => {
  //   vscode.languages.registerCompletionItemProvider(
  //     "python",
  //     {
  //       provideCompletionItems(
  //         document: vscode.TextDocument,
  //         position: vscode.Position,
  //       ) {
  //         const linePrefix = document
  //           .lineAt(position)
  //           .text.substr(0, position.character);
  //         // @ts-ignore
  //         const prefix = root2.find((a: string) => map23[a].includes(el));
  //         const prePrefix = root1.find((a: string) =>
  //           // @ts-ignore
  //           map12[a].includes(prefix),
  //         );

  //         if (!linePrefix.endsWith(prePrefix + "." + prefix + "." + el + ".")) {
  //           return undefined;
  //         }

  //         // @ts-ignore
  //         return map34[el]
  //           .filter((a: string | null) => a !== null)
  //           .map(
  //             (element: string) =>
  //               new vscode.CompletionItem(
  //                 element,
  //                 vscode.CompletionItemKind.Method,
  //               ),
  //           );
  //       },
  //     },
  //     ".",
  //   );
  // });

  // root4.forEach((el: string) => {
  //   vscode.languages.registerCompletionItemProvider(
  //     "python",
  //     {
  //       provideCompletionItems(
  //         document: vscode.TextDocument,
  //         position: vscode.Position,
  //       ) {
  //         const linePrefix = document
  //           .lineAt(position)
  //           .text.substr(0, position.character);
  //         // @ts-ignore
  //         const prefix = root3.find((a: string) => map34[a].includes(el));
  //         const prePrefix = root2.find((a: string) =>
  //           // @ts-ignore
  //           map23[a].includes(prefix),
  //         );
  //         const prePrePrefix = root1.find((a: string) =>
  //           // @ts-ignore
  //           map12[a].includes(prePrefix),
  //         );

  //         if (
  //           !linePrefix.endsWith(
  //             prePrePrefix + "." + prePrefix + "." + prefix + "." + el + ".",
  //           )
  //         ) {
  //           return undefined;
  //         }

  //         // @ts-ignore
  //         return map45[el]
  //           .filter((a: string | null) => a !== null)
  //           .map(
  //             (element: string) =>
  //               new vscode.CompletionItem(
  //                 element,
  //                 vscode.CompletionItemKind.Method,
  //               ),
  //           );
  //       },
  //     },
  //     ".",
  //   );
  // });

  context.subscriptions.push(keywords, hover);
}

export function deactivate() {}
