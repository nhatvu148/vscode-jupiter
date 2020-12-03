```{module} MidPlaneEdit.Face.FaceExtendtoFace()
:synopsis: add face by face extend to face
```

(MidPlaneEdit.Face.FaceExtendtoFace)=

# MidPlaneEdit.Face.FaceExtendtoFace

## Description

add face by face extend to face

## Syntax

```python
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemFaceByFaceExtend`

Ribbon: {menuselection}`MidPlaneEdit --> Face --> FaceExtendtoFace`

## Inputs

**`crlExtFaces`**
: A _Cursor List_ specifying the extend faces. This is a required input.

**`crlRefFaces`**
: A _Cursor List_ specifying the reference faces. This is a required input.

**`bMergeFace`**
: A _Boolean_ specifying the merge face. This is a required input.

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. This is a required input.

**`dMergeEdgeAngle`**
: A _Double_ specifying the merge edge angle. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```
