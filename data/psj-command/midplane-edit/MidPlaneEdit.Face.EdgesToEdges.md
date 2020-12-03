```{module} MidPlaneEdit.Face.EdgesToEdges()
:synopsis: add face by edges
```

(MidPlaneEdit.Face.EdgesToEdges)=

# MidPlaneEdit.Face.EdgesToEdges

## Description

add face by edges

## Syntax

```python
MidPlaneEdit.Face.EdgesToEdges(crlEdge, bImprint=False, bMultiEdges=False)
```

Macro: {ref}`Macro-MidPlaneEdit-GeometryAddItemFaceByEdges`

Ribbon: {menuselection}`MidPlaneEdit --> Face --> EdgesToEdges`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`bImprint`**
: A _Boolean_ specifying the imprint. The default value is False.

**`bMultiEdges`**
: A _Boolean_ specifying the multi edges. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.Face.EdgesToEdges(crlEdge, bImprint=False, bMultiEdges=False)
```
