```{module} MeshEdit.MoveNode.RefineQuality()
:synopsis: MeshEdit RefineQuality
```

(MeshEdit.MoveNode.RefineQuality)=

# MeshEdit.MoveNode.RefineQuality

## Description

MeshEdit RefineQuality

## Syntax

```python
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFace=[], crlElem=[], crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditMoveNodeRefineQuality`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> RefineQuality`

## Inputs

**`iMetric`**
: An _Integer_ specifying the metric. The default value is 0.

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFace=[], crlElem=[], crlNode=[])
```
