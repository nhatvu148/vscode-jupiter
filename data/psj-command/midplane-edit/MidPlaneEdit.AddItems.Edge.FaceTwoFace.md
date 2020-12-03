```{module} MidPlaneEdit.AddItems.Edge.FaceTwoFace()
:synopsis: Exent face to face
```

(MidPlaneEdit.AddItems.Edge.FaceTwoFace)=

# MidPlaneEdit.AddItems.Edge.FaceTwoFace

## Description

Exent face to face

## Syntax

```python
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemsEdgeExtendCylinderFace`

Ribbon: {menuselection}`MidPlaneEdit --> AddItems --> Edge --> FaceTwoFace`

## Inputs

**`crRefFace`**
: A _Cursor_ specifying the reference face. The default value is None.

**`crExtFace`**
: A _Cursor_ specifying the extend face. The default value is None.

**`iExtendType`**
: An _Integer_ specifying the extend type. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.AddItems.Edge.FaceTwoFace(crRefFace=None, crExtFace=None, iExtendType=0)
```
