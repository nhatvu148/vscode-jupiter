```{module} MidPlaneEdit.AddItems.Face.EFExtendFreeEdge()
:synopsis: Create new face by extend free edge to a destination face
```

(MidPlaneEdit.AddItems.Face.EFExtendFreeEdge)=

# MidPlaneEdit.AddItems.Face.EFExtendFreeEdge

## Description

Create new face by extend free edge to a destination face

## Syntax

```python
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdge, crlFace, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemFaceByEFExtend`

Ribbon: {menuselection}`MidPlaneEdit --> AddItems --> Face --> EFExtendFreeEdge`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`bMergeFace`**
: A _Boolean_ specifying the merge face. This is a required input.

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. This is a required input.

**`bUseNeighDir`**
: A _Boolean_ specifying the use neighborhood edge direction. This is a required input.

**`dMergeEdgeAngle`**
: A _Double_ specifying the merge edge angle. This is a required input.

**`bMultiEF`**
: A _Boolean_ specifying the multi edge and face . This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdge, crlFace, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
```
