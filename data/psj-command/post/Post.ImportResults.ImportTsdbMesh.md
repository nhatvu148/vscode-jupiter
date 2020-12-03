```{module} Post.ImportResults.ImportTsdbMesh()
:synopsis: import tsdb mesh
```

(Post.ImportResults.ImportTsdbMesh)=

# Post.ImportResults.ImportTsdbMesh

## Description

import tsdb mesh

## Syntax

```python
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Post-ImportTsdbMesh`

Ribbon: {menuselection}`Post --> ImportResults --> ImportTsdbMesh`

## Inputs

**`strTsdbFilePath`**
: A _String_ specifying the tsdb file path. This is a required input.

**`strBtxFilePath`**
: A _String_ specifying the btx file path. This is a required input.

**`iImportType`**
: An _Integer_ specifying the import type. The default value is 1.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```
