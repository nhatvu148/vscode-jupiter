```{module} Assemble.AssembleFace()
:synopsis: create assemble face
```

(Assemble.AssembleFace)=

# Assemble.AssembleFace

## Description

create assemble face

## Syntax

```python
Assemble.AssembleFace(crlPart, crlFace, dTolerance, iFitEdge, iMeshSetting)
```

Macro: {ref}`Macro-Assemble-ASMAssembleFace`

Ribbon: {menuselection}`Assemble --> AssembleFace`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`dTolerance`**
: A _Double_ specifying the tolerance. This is a required input.

**`iFitEdge`**
: An _Integer_ specifying the fit edge. This is a required input.

**`iMeshSetting`**
: An _Integer_ specifying the mesh setting. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.AssembleFace(crlPart, crlFace, dTolerance, iFitEdge, iMeshSetting)
```
