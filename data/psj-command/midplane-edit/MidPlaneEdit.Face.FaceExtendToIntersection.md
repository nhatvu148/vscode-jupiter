```{module} MidPlaneEdit.Face.FaceExtendToIntersection()
:synopsis: Face Extend To Intersection
```

(MidPlaneEdit.Face.FaceExtendToIntersection)=

# MidPlaneEdit.Face.FaceExtendToIntersection

## Description

Face Extend To Intersection

## Syntax

```python
MidPlaneEdit.Face.FaceExtendToIntersection(crEdge0, crEdge1)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemFaceByPlaneExtendIntersection`

Ribbon: {menuselection}`MidPlaneEdit --> Face --> FaceExtendToIntersection`

## Inputs

**`crEdge0`**
: A _Cursor_ specifying the edge0. This is a required input.

**`crEdge1`**
: A _Cursor_ specifying the edge1. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.Face.FaceExtendToIntersection(crEdge0, crEdge1)
```
