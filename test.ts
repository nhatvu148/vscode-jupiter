const fs = require("fs");
const Papa = require("papaparse");

let funcs: string[] = [];

class Node {
    public data: string;
    public parent: any | null;
    public children: any[];

    constructor(data: string) {
        this.data = data;
        this.parent = null;
        this.children = [];
    }
}

class Tree {
    public root: any;

    constructor(data: string) {
        this.root = new Node(data);
    }
}

const readPsjCommands = async () => {
    if (fs.existsSync(`${__dirname}/out/data/PSJCommandCalltips.dat`)) {
        const files = await fs.readFileSync(`${__dirname}/out/data/PSJCommandCalltips.dat`, "utf8");
        Papa.parse(files, {
            complete: function (results: any) {
                funcs = results.data.filter((a: string[]) => a[0].includes("Function:")).map((a: string[]) => a[0].substring(10));
                // console.log(funcs.forEach((a: string) => {
                //     if (a) {
                //         const arr = a.split(".");
                //         console.log(a);
                //         // for (let i = arr.length - 1; i > 0; i--) {
                //         //     console.log(a.slice(0, 1 * a.indexOf(arr[i])));
                //         //     console.log(arr[i])
                //         // }
                //     }
                // }));
                // const arr = funcs.map((f: string) => f.split("."));

                const arr = funcs.map((f: string) => f.split(".")).reduce((group: any, itm: any, idx: number, arr: any) => {
                    group[itm[0]] = group[itm[0]] ? [...group[itm[0]], itm.slice(1)] : [itm.slice(1)]
                    return group;
                }, {})
                console.log(funcs);
                let tree = new Tree('trunk');
                funcs.map((f: string) => f.split(".")).forEach((a: string[], i: any) => {
                    tree.root.children.push(new Node(a[0]));
                    tree.root.children[0].parent = tree;
                })

                console.log(tree.root);

            },
        });
    } else {
        console.log(__dirname);
    }
}

readPsjCommands();