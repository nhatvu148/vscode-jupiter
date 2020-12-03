```{module} Post.ImportResults.ImportOp2Mesh()
:synopsis: import Nastran op2 mesh
```

(Post.ImportResults.ImportOp2Mesh)=

# Post.ImportResults.ImportOp2Mesh

## Description

import Nastran op2 mesh

## Syntax

```python
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Post-ImportOp2Mesh`

Ribbon: {menuselection}`Post --> ImportResults --> ImportOp2Mesh`

## Inputs

**`strlFilePaths`**
: A _String List_ specifying the file paths. This is a required input.

**`iImportType`**
: An _Integer_ specifying the import type. The default value is 0.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```
