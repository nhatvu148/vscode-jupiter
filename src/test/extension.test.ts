import * as assert from "assert";
import * as vscode from "vscode";
import { findEnclosingCall } from "../extension";
import { allApiEntries, allKeywords, lookupApi } from "../jupiterApi";

const EXTENSION_ID = "nhatvu148.jupiter";

suite("jupiterApi", () => {
  test("exposes the merged API surface (~1800+ entries)", () => {
    assert.ok(
      allApiEntries().length > 1800,
      `expected >1800 entries, got ${allApiEntries().length}`,
    );
  });

  test("provides an accurate signature + typed params for a known command", () => {
    const entry = lookupApi("FileMenu.AddJTDB");
    assert.ok(entry, "FileMenu.AddJTDB should be a known API entry");
    assert.strictEqual(entry.prefix, "AddJTDB");
    assert.match(entry.signature, /^FileMenu\.AddJTDB\(strFileName/); // real signature
    assert.match(entry.doc, /strFileName/); // shown in the param table
    assert.match(entry.doc, /\(String\)/); // inferred type, our own derivation
    assert.doesNotMatch(entry.doc, /## Description/); // no bundled vendor prose
  });

  test("knows a JPT utility from Utility.py", () => {
    const entry = lookupApi("JPT.GetThicknessOfEntity");
    assert.ok(entry, "JPT.GetThicknessOfEntity should be known");
    assert.match(entry.signature, /^JPT\.GetThicknessOfEntity\(/);
  });

  test("returns undefined for an unknown name", () => {
    assert.strictEqual(lookupApi("Totally.Made.Up.Zzzqqq999"), undefined);
  });

  test("resolves a GUI builder method by leaf name", () => {
    const entry = lookupApi("dlg.add_button"); // instance-style call
    assert.ok(entry, "dlg.add_button should resolve to JDGCreator.add_button");
    assert.match(entry.signature, /add_button\(/);
    assert.ok(entry.params.includes("layout"));
  });

  test("exposes PSJ utility + GUI keywords", () => {
    const labels = new Set(allKeywords().map((k) => k.label));
    assert.ok(labels.has("add_button"), "GUI keyword add_button missing");
    assert.ok(allKeywords().length > 500);
  });
});

suite("findEnclosingCall", () => {
  test("returns the call name with no args typed yet", () => {
    const r = findEnclosingCall("    FileMenu.AddJTDB(");
    assert.deepStrictEqual(r, { name: "FileMenu.AddJTDB", activeParam: 0 });
  });

  test("counts top-level commas for the active parameter", () => {
    const r = findEnclosingCall('FileMenu.AddJTDB("a", "AUTO", ');
    assert.strictEqual(r?.name, "FileMenu.AddJTDB");
    assert.strictEqual(r?.activeParam, 2);
  });

  test("ignores commas inside nested calls", () => {
    const r = findEnclosingCall("Foo.Bar(x, baz(1, 2), ");
    assert.strictEqual(r?.name, "Foo.Bar");
    assert.strictEqual(r?.activeParam, 2);
  });

  test("returns undefined when not inside a call", () => {
    assert.strictEqual(findEnclosingCall("x = 1 + 2"), undefined);
  });
});

suite("extension", () => {
  test("is present and activates", async () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext, `extension ${EXTENSION_ID} should be installed`);
    await ext.activate();
    assert.strictEqual(ext.isActive, true);
  });
});
