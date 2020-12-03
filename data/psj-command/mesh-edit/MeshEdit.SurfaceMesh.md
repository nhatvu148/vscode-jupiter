```{module} MeshEdit.SurfaceMesh()
:synopsis: Element Conversion
```

(MeshEdit.SurfaceMesh)=

# MeshEdit.SurfaceMesh

## Description

Element Conversion

## Syntax

```python
MeshEdit.SurfaceMesh(crlPart=[], iType=1)
```

Macro: {ref}`Macro-MeshEdit-ElementConv_Surface`

Ribbon: {menuselection}`MeshEdit --> SurfaceMesh`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`iType`**
: An _Integer_ specifying the type. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.SurfaceMesh(crlPart=[], iType=1)
```
