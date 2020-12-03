```{module} MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace()
:synopsis: project an edge to face to get a new edge
```

(MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace)=

# MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace

## Description

project an edge to face to get a new edge

## Syntax

```python
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdge, crlFace, bExtendEdge=True)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemsEdgeProjectEdgetoFaceCr`

Ribbon: {menuselection}`MidPlaneEdit --> AddItems --> Edge --> ProjectEdgeToFace`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`bExtendEdge`**
: A _Boolean_ specifying the extend edge. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdge, crlFace, bExtendEdge=True)
```
