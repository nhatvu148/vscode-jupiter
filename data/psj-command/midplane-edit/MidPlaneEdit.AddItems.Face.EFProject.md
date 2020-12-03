```{module} MidPlaneEdit.AddItems.Face.EFProject()
:synopsis: Creat new face by project edge to destination face
```

(MidPlaneEdit.AddItems.Face.EFProject)=

# MidPlaneEdit.AddItems.Face.EFProject

## Description

Creat new face by project edge to destination face

## Syntax

```python
MidPlaneEdit.AddItems.Face.EFProject(crlEdge, crlFace, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemFaceByEFProject`

Ribbon: {menuselection}`MidPlaneEdit --> AddItems --> Face --> EFProject`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`bMergeFace`**
: A _Boolean_ specifying the merge face. This is a required input.

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. This is a required input.

**`dMergeEdgeAngle`**
: A _Double_ specifying the merge edge angle. This is a required input.

**`bMultiEF`**
: A _Boolean_ specifying the multi edge and face . This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.AddItems.Face.EFProject(crlEdge, crlFace, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```
