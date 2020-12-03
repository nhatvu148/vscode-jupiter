```{module} Meshing.SetAttib()
:synopsis: set attribute
```

(Meshing.SetAttib)=

# Meshing.SetAttib

## Description

set attribute

## Syntax

```python
Meshing.SetAttib(crlPart = [], surfaceMesh = SURFACE_MESH())
```

Macro: {ref}`Macro-Meshing-SetMeshAttrib`

Ribbon: {menuselection}`Meshing --> SetAttib`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`surfaceMesh`**
: A _SURFACE_MESH_ specifying the mesh. The default value is SURFACE_MESH().

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.SetAttib(crlPart = [], surfaceMesh = SURFACE_MESH())
```
