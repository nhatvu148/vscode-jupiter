```{module} MeshEdit.Face()
:synopsis: Make Mesh deformation
```

(MeshEdit.Face)=

# MeshEdit.Face

## Description

Make Mesh deformation

## Syntax

```python
MeshEdit.Face(crlFace, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditMorphingFaces`

Ribbon: {menuselection}`MeshEdit --> Face`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlFaceFixed`**
: A _Cursor List_ specifying the face fixed. This is a required input.

**`iOffsetType`**
: An _Integer_ specifying the offset type. The default value is 0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dlOffset`**
: A _Double List_ specifying the offset. The default value is [1.0, 0.0, 0.0].

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.

**`iDistType`**
: An _Integer_ specifying the dist type. The default value is 0.

**`dDistStrong`**
: A _Double_ specifying the dist strong. The default value is 10.

**`dDistWeak`**
: A _Double_ specifying the dist weak. The default value is 20.

**`iNodeIdPick`**
: An _Integer_ specifying the node ID pick. The default value is -1.

**`dlPickForMacro`**
: A _Double List_ specifying the pick for macro. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.Face(crlFace, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```
