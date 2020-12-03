```{module} MeshEdit.RemoveSolidMesh()
:synopsis: Remove Solid Mesh
```

(MeshEdit.RemoveSolidMesh)=

# MeshEdit.RemoveSolidMesh

## Description

Remove Solid Mesh

## Syntax

```python
MeshEdit.RemoveSolidMesh(crlPart=[], bConvFirst=False)
```

Macro: {ref}`Macro-MeshEdit-RemoveSolidMesh`

Ribbon: {menuselection}`MeshEdit --> RemoveSolidMesh`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bConvFirst`**
: A _Boolean_ specifying the conv first. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.RemoveSolidMesh(crlPart=[], bConvFirst=False)
```
