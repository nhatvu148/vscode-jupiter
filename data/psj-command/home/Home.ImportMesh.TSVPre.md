```{module} Home.ImportMesh.TSVPre()
:synopsis: Convert a old TSV-Pre/Designer file into one or more jtdb files.
```

(Home.ImportMesh.TSVPre)=

# Home.ImportMesh.TSVPre

## Description

Convert a old TSV-Pre/Designer file into one or more jtdb files.

## Syntax

```python
Home.ImportMesh.TSVPre(strImportPath="", strExportPath="", ilModelIndex=None, iMerge=None)
```

Macro: {ref}`Macro-Home-ImportVDB`

Ribbon: {menuselection}`Home --> ImportMesh --> TSVPre`

## Inputs

**`strImportPath`**
: A _String_ specifying the import path. The default value is "".

**`strExportPath`**
: A _String_ specifying the export path. The default value is "".

**`ilModelIndex`**
: A _Integer List_ specifying the model index. The default value is None.

**`iMerge`**
: An _Integer_ specifying the merge. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportMesh.TSVPre(strImportPath="", strExportPath="", ilModelIndex=None, iMerge=None)
```
