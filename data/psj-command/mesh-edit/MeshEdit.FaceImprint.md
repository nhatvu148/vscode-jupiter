```{module} MeshEdit.FaceImprint()
:synopsis: import Nastran bdf file
```

(MeshEdit.FaceImprint)=

# MeshEdit.FaceImprint

## Description

import Nastran bdf file

## Syntax

```python
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```

Macro: {ref}`Macro-MeshEdit-MeshEditCMPFaceImprint`

Ribbon: {menuselection}`MeshEdit --> FaceImprint`

## Inputs

**`crlFaces`**
: A _Cursor List_ specifying the faces. The default value is [].

**`bMeshCopy`**
: A _Boolean_ specifying the mesh copy. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```
