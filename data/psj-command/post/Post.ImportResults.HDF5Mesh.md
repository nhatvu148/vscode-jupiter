```{module} Post.ImportResults.HDF5Mesh()
:synopsis: import Nastran HDF5Mesh file
```

(Post.ImportResults.HDF5Mesh)=

# Post.ImportResults.HDF5Mesh

## Description

import Nastran HDF5Mesh file

## Syntax

```python
Post.ImportResults.HDF5Mesh(strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Post-ImportHDF5Mesh`

Ribbon: {menuselection}`Post --> ImportResults --> HDF5Mesh`

## Inputs

**`strlFilePaths`**
: A _String List_ specifying the file paths. This is a required input.

**`iImportType`**
: An _Integer_ specifying the import type. The default value is 2.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.HDF5Mesh(strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0)
```
