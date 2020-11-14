const fs = require("fs");
const Papa = require("papaparse");

let libKey: string[] = [];
let psjUtilKeys: string[] = [];
let psjGuiKeys: string[] = [];
let funcs: string[] = [];

const readKeywords = async () => {
  if (fs.existsSync(`${__dirname}/data/Keywords.dat`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/Keywords.dat`,
      "utf8"
    );
    Papa.parse(files, {
      complete: function (results: any) {
        libKey = results.data[6];
        psjUtilKeys = results.data[9];
        psjGuiKeys = results.data[12];
        fs.writeFile(
          `${__dirname}/data/libKey.txt`,
          JSON.stringify(libKey),
          function (err: any) {
            if (err) return console.log(err);
          }
        );
        fs.writeFile(
          `${__dirname}/data/psjUtilKeys.txt`,
          JSON.stringify(psjUtilKeys),
          function (err: any) {
            if (err) return console.log(err);
          }
        );
        fs.writeFile(
          `${__dirname}/data/psjGuiKeys.txt`,
          JSON.stringify(psjGuiKeys),
          function (err: any) {
            if (err) return console.log(err);
          }
        );
      },
    });
  } else {
    console.log(__dirname);
  }
};

const readPsjCommands = async () => {
  if (fs.existsSync(`${__dirname}/data/PSJCommandCalltips.dat`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/PSJCommandCalltips.dat`,
      "utf8"
    );
    Papa.parse(files, {
      complete: function (results: any) {
        funcs = results.data
          .filter((a: string[]) => a[0].includes("Function:"))
          .map((a: string[]) => a[0].substring(10));

        const arr = funcs
          .map((f: string) => f.split("."))
          .reduce((group: any, itm: any, idx: number, arr: any) => {
            group[itm[0]] = group[itm[0]]
              ? [...group[itm[0]], itm.slice(1)]
              : [itm.slice(1)];
            return group;
          }, {});

        const group1 = funcs
          .map((f: string) => f.split("."))
          .reduce((group: any, itm: any, idx: number, arr: any) => {
            group[itm[0]] = group[itm[0]]
              ? [...group[itm[0]], itm[1]]
              : [itm[1]];
            return group;
          }, {});

        Object.keys(group1).forEach((o: any) => {
          group1[o] = [...new Set(group1[o])];
        });

        const group2 = funcs
          .map((f: string) => f.split("."))
          .reduce((group: any, itm: any, idx: number, arr: any) => {
            group[itm[1]] = group[itm[1]]
              ? [...group[itm[1]], itm[2]]
              : [itm[2]];
            return group;
          }, {});

        Object.keys(group2).forEach((o: any) => {
          group2[o] = [...new Set(group2[o])];
        });

        fs.writeFile(
          `${__dirname}/data/root2.txt`,
          JSON.stringify(Object.keys(group2)),
          function (err: any) {
            if (err) return console.log(err);
            console.log("Hello World > root2.txt");
          }
        );

        // fs.writeFile(
        //   `${__dirname}/data/map23.txt`,
        //   JSON.stringify(group2),
        //   function (err: any) {
        //     if (err) return console.log(err);
        //     console.log("Hello World > map23.txt");
        //   }
        // );

        console.log(Object.keys(group1));
      },
    });
  } else {
    console.log(__dirname);
  }
};

readKeywords();
readPsjCommands();
