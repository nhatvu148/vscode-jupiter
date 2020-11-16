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
      "utf8",
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
          },
        );
        fs.writeFile(
          `${__dirname}/data/psjUtilKeys.txt`,
          JSON.stringify(psjUtilKeys),
          function (err: any) {
            if (err) return console.log(err);
          },
        );
        fs.writeFile(
          `${__dirname}/data/psjGuiKeys.txt`,
          JSON.stringify(psjGuiKeys),
          function (err: any) {
            if (err) return console.log(err);
          },
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
      "utf8",
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

        const group3 = funcs
          .map((f: string) => f.split("."))
          .reduce((group: any, itm: any, idx: number, arr: any) => {
            group[itm[2]] = group[itm[2]]
              ? [...group[itm[2]], itm[3]]
              : [itm[3]];
            return group;
          }, {});

        Object.keys(group3).forEach((o: any) => {
          group3[o] = [...new Set(group3[o])];
        });

        const group4 = funcs
          .map((f: string) => f.split("."))
          .reduce((group: any, itm: any, idx: number, arr: any) => {
            group[itm[3]] = group[itm[3]]
              ? [...group[itm[3]], itm[4]]
              : [itm[4]];
            return group;
          }, {});

        Object.keys(group4).forEach((o: any) => {
          group4[o] = [...new Set(group4[o])];
        });

        // fs.writeFile(
        //   `${__dirname}/data/root4.txt`,
        //   JSON.stringify(Object.keys(group4)),
        //   function (err: any) {
        //     if (err) return console.log(err);
        //     console.log("Hello World > root4.txt");
        //   }
        // );

        fs.writeFile(
          `${__dirname}/data/map45.txt`,
          JSON.stringify(group4),
          function (err: any) {
            if (err) return console.log(err);
            console.log("Hello World > map45.txt");
          },
        );

        console.log(Object.keys(group1));
      },
    });
  } else {
    console.log(__dirname);
  }
};

const readPSJSnippets = async () => {
  if (fs.existsSync(`${__dirname}/data/PSJCommands.txt`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/PSJCommands.txt`,
      "utf8",
    );
    Papa.parse(files, {
      complete: function (results: any) {
        const res = results.data;
        const snippets = res.reduce((obj: any, cur: any, idx: number) => {
          const fnName = cur[0].split("(")[0];
          if (obj[fnName]) {
            return obj;
          } else {
            let i = 1;
            const modCur = cur
              .join()
              .split("=")
              .map((a: string, index: number, arr: string[]) => {
                if (index === 0) {
                  return a;
                } else if (index !== arr.length - 1) {
                  const val = a.match(/.*(?=\,)/);
                  if (val !== null) {
                    const mod = a.replace(val[0], `\${${i}:${val[0]}}`);
                    i++;
                    return mod;
                  } else {
                    return a;
                  }
                } else {
                  const val = a.match(/.*(?=\))/);
                  if (val !== null) {
                    const mod = a.replace(val[0], `\${${i}:${val[0]}}`);
                    i++;
                    return mod;
                  } else {
                    return a;
                  }
                }
              });

            return {
              ...obj,
              [fnName]: {
                prefix: `${fnName}`,
                body: modCur.join("="),
                description: `Code snippet for ${fnName}`,
              },
            };
          }
        }, {});

        console.log(snippets);

        fs.writeFile(
          `${__dirname}/data/psjSnippets.txt`,
          JSON.stringify(snippets),
          function (err: any) {
            if (err) return console.log(err);
          },
        );
      },
    });
  } else {
    console.log(__dirname);
  }
};

// readKeywords();
// readPsjCommands();
readPSJSnippets();
