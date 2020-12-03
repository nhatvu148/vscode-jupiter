```{module} Geometry.Face.FromMesh()
:synopsis: Create geometry face from mesh face
```

(Geometry.Face.FromMesh)=

# Geometry.Face.FromMesh

## Description

Create geometry face from mesh face

## Syntax

```python
Geometry.Face.FromMesh(crlFace)
```

Macro: {ref}`Macro-Geometry-CreateFaceFromMeshFace`

Ribbon: {menuselection}`Geometry --> Face --> FromMesh`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Face.FromMesh(crlFace)
```
