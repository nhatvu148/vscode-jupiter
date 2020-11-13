import * as vscode from 'vscode';
const fs = require("fs");
const Papa = require("papaparse");

let libKey: string[] = [];
let psjUtilKeys: string[] = [];
let psjGuiKeys: string[] = [];
let funcs: string[] = [];

const readKeywords = async () => {
    if (fs.existsSync(`${__dirname}/data/Keywords.dat`)) {
        const files = await fs.readFileSync(`${__dirname}/data/Keywords.dat`, "utf8");
        Papa.parse(files, {
            complete: function (results: any) {
                libKey = results.data[6]
                psjUtilKeys = results.data[9]
                psjGuiKeys = results.data[12]
                // console.log(libKey, psjUtilKeys, psjGuiKeys);
                // console.log(results);
            },
        });
    } else {
        console.log(__dirname);
    }
}

const readPsjCommands = async () => {
    if (fs.existsSync(`${__dirname}/data/PSJCommandCalltips.dat`)) {
        const files = await fs.readFileSync(`${__dirname}/data/PSJCommandCalltips.dat`, "utf8");
        Papa.parse(files, {
            complete: function (results: any) {
                funcs = results.data.filter((a: string[]) => a[0].includes("Function:")).map((a: string[]) => a[0].substring(10));
                console.log(funcs.forEach((a: string) => {
                    if (a) {
                        const arr = a.split(".");
                        console.log(a);
                        // for (let i = arr.length - 1; i > 0; i--) {
                        //     console.log(a.slice(0, 1 * a.indexOf(arr[i])));
                        //     console.log(arr[i])
                        // }
                    }
                }));
            },
        });
    } else {
        console.log(__dirname);
    }
}

export function activate(context: vscode.ExtensionContext) {
    readKeywords();
    readPsjCommands();

    const provider1 = vscode.languages.registerCompletionItemProvider('*', {

        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken, context: vscode.CompletionContext) {

            // a simple completion item which inserts `Hello World!`
            const simpleCompletion = new vscode.CompletionItem('Hello World!');

            // a completion item that inserts its text as snippet,
            // the `insertText`-property is a `SnippetString` which will be
            // honored by the editor.
            const snippetCompletion = new vscode.CompletionItem('Good part of the day');
            snippetCompletion.insertText = new vscode.SnippetString('Good ${1|morning,afternoon,evening|}. It is ${1}, right?');
            snippetCompletion.documentation = new vscode.MarkdownString("Inserts a snippet that lets you select the _appropriate_ part of the day for your greeting.");

            // a completion item that can be accepted by a commit character,
            // the `commitCharacters`-property is set which means that the completion will
            // be inserted and then the character will be typed.
            const commitCharacterCompletion = new vscode.CompletionItem('Analysis');
            commitCharacterCompletion.commitCharacters = ['.'];
            commitCharacterCompletion.documentation = new vscode.MarkdownString('Press `.` to get `console.`');

            // a completion item that retriggers IntelliSense when being accepted,
            // the `command`-property is set which the editor will execute after 
            // completion has been inserted. Also, the `insertText` is set so that 
            // a space is inserted after `new`
            const commandCompletion = new vscode.CompletionItem('new');
            commandCompletion.kind = vscode.CompletionItemKind.Keyword;
            commandCompletion.insertText = 'new ';
            commandCompletion.command = { command: 'editor.action.triggerSuggest', title: 'Re-trigger completions...' };

            // return all completion items as array
            return [
                simpleCompletion,
                snippetCompletion,
                commitCharacterCompletion,
                commandCompletion
            ];
        }
    });

    const hover = vscode.languages.registerHoverProvider('*', {
        provideHover(document, position, token) {
            return new vscode.Hover("Some comments");
        }
    });

    const keywords = vscode.languages.registerCompletionItemProvider('*', {
        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken) {
            const libKeyList = libKey.map((a) => new vscode.CompletionItem(a))
            const psjUtilKeyList = psjUtilKeys.map((a) => new vscode.CompletionItem(a))
            const psjGuiKeyList = psjGuiKeys.map((a) => new vscode.CompletionItem(a))
            return [...libKeyList, ...psjUtilKeyList, ...psjGuiKeyList];
        }
    });

    // const psjCommands = vscode.languages.registerCompletionItemProvider(
    //     '*',
    //     {
    //         provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {

    //             // get all text until the `position` and check if it reads `console.`
    //             // and if so then complete if `log`, `warn`, and `error`
    //             const linePrefix = document.lineAt(position).text.substr(0, position.character);
    //             if (!linePrefix.endsWith('Analysis.')) {
    //                 return undefined;
    //             }

    //             return [
    //                 new vscode.CompletionItem('Abaqus', vscode.CompletionItemKind.Method),
    //                 new vscode.CompletionItem('AbaqusStep', vscode.CompletionItemKind.Method),
    //                 new vscode.CompletionItem('ACTRAN', vscode.CompletionItemKind.Method),
    //             ];
    //         }
    //     },
    //     '.' // triggered whenever a '.' is being typed
    // );

    const psjCommands2 = vscode.languages.registerCompletionItemProvider('*', {
        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken) {
            const funcList = funcs.map((a) => new vscode.CompletionItem(a))
            return funcList;
        }
    });

    funcs.forEach((a: string) => {
        const arr = a.split(".");
        if (a) {
            for (let i = arr.length - 1; i > 0; i--) {
                context.subscriptions.push(vscode.languages.registerCompletionItemProvider(
                    '*',
                    {
                        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {
                            const linePrefix = document.lineAt(position).text.substr(0, position.character);
                            console.log(a.slice(0, 1 * a.indexOf(arr[i])))
                            if (!linePrefix.endsWith(`${a.slice(0, -1 * a.indexOf(arr[i]))}`)) {
                                return undefined;
                            }

                            return [
                                new vscode.CompletionItem(`${arr[i]}`, vscode.CompletionItemKind.Method),
                            ];
                        }
                    },
                    '.'
                ))
            }
        }

    });

    // const psjCommands3 = vscode.languages.registerCompletionItemProvider(
    //     '*',
    //     {
    //         provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {

    //             // get all text until the `position` and check if it reads `console.`
    //             // and if so then complete if `log`, `warn`, and `error`
    //             const linePrefix = document.lineAt(position).text.substr(0, position.character);
    //             if (!linePrefix.endsWith('Analysis.Abaqus.')) {
    //                 return undefined;
    //             }

    //             return [
    //                 new vscode.CompletionItem('heelo', vscode.CompletionItemKind.Method),
    //                 new vscode.CompletionItem('heelo2', vscode.CompletionItemKind.Method),
    //                 new vscode.CompletionItem('heeloACTRAN2', vscode.CompletionItemKind.Method),
    //             ];
    //         }
    //     },
    //     '.' // triggered whenever a '.' is being typed
    // );

    context.subscriptions.push(vscode.languages.registerCompletionItemProvider('*', {
        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken) {
            return [new vscode.CompletionItem("Nhat Vu")];
        }
    }));
    context.subscriptions.push(keywords, psjCommands2, hover);
}

export function deactivate() { }