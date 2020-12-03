```{module} Geometry.MergeEntities.Faces()
:synopsis: Merge faces
```

(Geometry.MergeEntities.Faces)=

# Geometry.MergeEntities.Faces

## Description

Merge faces

## Syntax

```python
Geometry.MergeEntities.Faces(crlFace=[], bMergeEdge=True, bRemoveNonBoundEdge=True)
```

Macro: {ref}`Macro-Geometry-MergeFace_MergeEntities`

Ribbon: {menuselection}`Geometry --> MergeEntities --> Faces`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. The default value is True.

**`bRemoveNonBoundEdge`**
: A _Boolean_ specifying the remove non boundary edge. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MergeEntities.Faces(crlFace=[], bMergeEdge=True, bRemoveNonBoundEdge=True)
```
