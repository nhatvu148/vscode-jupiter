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

const stringManipulate = (val: any, a: string, i: number[]) => {
  if (val !== null) {
    if (val[0].startsWith('"')) {
      const content = val[0].match(/(?<=\").*(?=\")/);
      if (content !== null) {
        const mod = a.replace(`"${content[0]}"`, `"\${${i[0]}:${content[0]}}"`);
        i[0]++;
        return mod;
      }
    } else if (val[0].startsWith("[")) {
      const content = val[0].match(/(?<=\[).*(?=\])/);
      if (content !== null) {
        if (content[0] !== "") {
          const _content = content[0]
            .split(",")
            .map((c: string) => {
              const _c = `\${${i[0]}:${c}}`;
              i[0]++;
              return _c;
            })
            .join(",");
          const mod = a.replace(`[${content[0]}]`, `[${_content}]`);
          return mod;
        } else {
          const mod = a.replace(
            `[${content[0]}]`,
            `[\${${i[0]}:${content[0]}}]`,
          );
          i[0]++;
          return mod;
        }
      }
    } else {
      const mod = a.replace(val[0], `\${${i[0]}:${val[0]}}`);
      i[0]++;
      return mod;
    }
  } else {
    return a;
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
            let i = [1];
            const modCur = cur
              .join()
              .split("=")
              .map((a: string) => a.trim())
              .map((a: string, index: number, arr: string[]) => {
                if (index === 0) {
                  return a;
                } else if (index !== arr.length - 1) {
                  const val = a.match(/.*(?=\,)/);
                  return stringManipulate(val, a, i);
                } else {
                  const val = a.match(/.*(?=\))/);
                  return stringManipulate(val, a, i);
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

const readPSJCallTips = async () => {
  if (fs.existsSync(`${__dirname}/data/PSJCommandCalltips.txt`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/PSJCommandCalltips.txt`,
      "utf8",
    );
    Papa.parse(files, {
      delimiter: ":)))",
      complete: function (results: any) {
        const res = results.data;

        // const obj = {
        //   "FileMenu.AddJTDB":
        //     "Name: FileMenu.AddJTDB\nDesc: add jtdb into model\nJVer: 5.0",
        // };
        const obj = res.reduce(
          (arr: any, cur: string[], idx: number, bigArr: any) => {
            if (idx === bigArr.length - 1) {
              return arr[1];
            }
            if (cur[0].startsWith("Name:")) {
              const match = cur[0].match(/(?<=\.)[A-Za-z_]*$/);
              const mod = cur[0].match(/^.*(?=:)/);

              if (match !== null && mod !== null && match[0] !== "") {
                arr[0] = cur[0].replace(mod[0] + ": ", "");
                const fnName = match[0];
                const _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);
                arr[1][arr[0]] = {
                  prefix: fnName,
                  text: _newCur0 + "  \n",
                };
              }
              return arr;
            } else if (cur[0].startsWith("-----")) {
              return arr;
            } else {
              const mod = cur[0].match(/^.*(?=:)/);
              let _newCur0 = cur[0];
              if (mod !== null) {
                _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);
              }
              arr[1][arr[0]].text = arr[1][arr[0]].text.concat(
                _newCur0 + "  \n ",
              );
              return arr;
            }
          },
          ["", {}],
        );
        console.log(obj);

        fs.writeFile(
          `${__dirname}/data/psjCallTips.txt`,
          JSON.stringify(obj),
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
// readPSJSnippets();
// readPSJCallTips();

// function* getNames() {
//   console.log("2");
//   yield "John";
//   console.log("4");
//   let myVal = yield "Stephanie";
//   console.log(`6. Passed in value: ${myVal}`);
// }

// const nameGen = getNames();
// console.log("1");
// console.log(`3. ${nameGen.next().value}`);
// console.log(`5. ${nameGen.next().value}`);
// console.log(`7. Done?${nameGen.next(999).done}`);

const psjUtilityCalltips = async () => {
  if (fs.existsSync(`${__dirname}/data/PSJUtilityCalltips.dat`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/PSJUtilityCalltips.dat`,
      "utf8",
    );
    Papa.parse(files, {
      delimiter: ":)))",
      complete: function (results: any) {
        const res = results.data;
        const obj = res.reduce(
          (arr: any, cur: string[], idx: number, bigArr: any) => {
            if (idx === bigArr.length - 1) {
              return arr[1];
            }
            if (cur[0].startsWith("Function:")) {
              const match = cur[0].match(/(?<=\.)[A-Za-z_1-9]*$/);
              const mod = cur[0].match(/^.*(?=:)/);

              if (match !== null && mod !== null && match[0] !== "") {
                arr[0] = cur[0].replace(mod[0] + ": ", "");
                const fnName = match[0];
                const _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);
                arr[1][arr[0]] = {
                  prefix: fnName,
                  text: _newCur0 + "  \n",
                };
              }
              return arr;
            } else if (cur[0].startsWith("-----")) {
              return arr;
            } else {
              const mod = cur[0].match(/^.*(?=:)/);
              let _newCur0 = cur[0];
              if (mod !== null) {
                _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);
              }
              arr[1][arr[0]].text = arr[1][arr[0]].text.concat(
                _newCur0 + "  \n ",
              );
              return arr;
            }
          },
          ["", {}],
        );

        console.log(obj);

        fs.writeFile(
          `${__dirname}/data/psjUtilityCallTips.txt`,
          JSON.stringify(obj),
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
// psjUtilityCalltips();

const psjUtilityCalltipsPython = async () => {
  if (fs.existsSync(`${__dirname}/data/PSJUtilityCalltips.dat`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/PSJUtilityCalltips.dat`,
      "utf8",
    );
    Papa.parse(files, {
      delimiter: ":)))",
      complete: function (results: any) {
        const res = results.data;
        const obj = res.reduce(
          (arr: any, cur: string[], idx: number, bigArr: any) => {
            if (idx === bigArr.length - 1) {
              return arr[1];
            }

            if (cur[0].startsWith("Function:")) {
              const match = cur[0].match(/(?<=\.)[A-Za-z_1-9]*$/);
              const mod = cur[0].match(/^.*(?=:)/);

              if (match !== null && mod !== null && match[0] !== "") {
                arr[0] = cur[0].replace(mod[0] + ": ", "");
                const fnName = match[0];
                const _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);
                arr[2] = [];

                arr[1][arr[0]] = {
                  prefix: fnName,
                  text: _newCur0 + "  \n",
                  params: arr[2],
                };
              }
              return arr;
            } else if (cur[0].startsWith("-----")) {
              return arr;
            } else {
              const mod = cur[0].match(/^.*(?=:)/);
              let _newCur0 = cur[0];
              if (mod !== null) {
                _newCur0 = cur[0].replace(mod[0] + ":", `*${mod[0]}:*`);

                if (cur[0].startsWith("Input1: None")) {
                  arr[2] = [];
                } else if (mod[0].startsWith("Input")) {
                  if (cur[0].includes("string")) {
                    arr[2].push(mod[0] + "_str");
                  } else {
                    arr[2].push(mod[0]);
                  }
                }
              }
              arr[1][arr[0]].text = arr[1][arr[0]].text.concat(
                _newCur0 + "  \n ",
              );
              arr[1][arr[0]].params = arr[2];
              return arr;
            }
          },
          ["", {}, []],
        );

        console.log(obj);
        Object.keys(obj).forEach((a: any) => {
          fs.appendFile(
            `${__dirname}/data/Jupiter.py`,
            `def ${obj[a].prefix}(${obj[a].params}):\n    message = "${a}(${obj[
              a
            ].params.map((b: string) =>
              b.includes("_str") ? "'{}'" : "{}",
            )})".format(${
              obj[a].params
            })\n    return JPT_RUN_LINE(message)\n\n`,
            function (err: any) {
              if (err) throw err;
            },
          );
        });

        // fs.writeFile(
        //   `${__dirname}/data/psjUtilityCallTips.txt`,
        //   JSON.stringify(obj),
        //   function (err: any) {
        //     if (err) return console.log(err);
        //   },
        // );
      },
    });
  } else {
    console.log(__dirname);
  }
};
// psjUtilityCalltipsPython();

const readPSJCommandsPython = async () => {
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
            let i = [1];
            const modCur = cur
              .join()
              .split("=")
              .map((a: string) => a.trim())
              .map((a: string, index: number, arr: string[]) => {
                if (index === 0) {
                  return a;
                } else if (index !== arr.length - 1) {
                  const val = a.match(/.*(?=\,)/);
                  return stringManipulate(val, a, i);
                } else {
                  const val = a.match(/.*(?=\))/);
                  return stringManipulate(val, a, i);
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

        // fs.writeFile(
        //   `${__dirname}/data/psjSnippets.txt`,
        //   JSON.stringify(snippets),
        //   function (err: any) {
        //     if (err) return console.log(err);
        //   },
        // );
      },
    });
  } else {
    console.log(__dirname);
  }
};
// readPSJCommandsPython()
const readEntityType = async () => {
  if (fs.existsSync(`${__dirname}/data/EntityType.txt`)) {
    const files = await fs.readFileSync(
      `${__dirname}/data/EntityType.txt`,
      "utf8",
    );
    Papa.parse(files, {
      complete: function (results: any) {
        const res = results.data;

        const res2 = res.map((a: string[]) => {
          const [a1, a2] = a[0].split(":");
          return a2.split(".")[2] + " = " + a1;
        });

        console.log(res2);

        res2.forEach((element: any) => {
          fs.appendFile(
            `${__dirname}/data/EntityType2.txt`,
            element + "\n",
            function (err: any) {
              if (err) throw err;
            },
          );
        });
      },
    });
  } else {
    console.log(__dirname);
  }
};
readEntityType();
