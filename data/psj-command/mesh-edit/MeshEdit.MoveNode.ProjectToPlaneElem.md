```{module} MeshEdit.MoveNode.ProjectToPlaneElem()
:synopsis: Move Node by Project to Plane(Elem)
```

(MeshEdit.MoveNode.ProjectToPlaneElem)=

# MeshEdit.MoveNode.ProjectToPlaneElem

## Description

Move Node by Project to Plane(Elem)

## Syntax

```python
MeshEdit.MoveNode.ProjectToPlaneElem(crlNode=[], crlElem=[])
```

Macro: {ref}`Macro-MeshEdit-MoveNodeNode2PlanElemCr`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> ProjectToPlaneElem`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.ProjectToPlaneElem(crlNode=[], crlElem=[])
```
