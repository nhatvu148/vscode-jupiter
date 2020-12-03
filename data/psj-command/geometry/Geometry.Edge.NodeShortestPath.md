```{module} Geometry.Edge.NodeShortestPath()
:synopsis: create edge by 2 nodes shortest path
```

(Geometry.Edge.NodeShortestPath)=

# Geometry.Edge.NodeShortestPath

## Description

create edge by 2 nodes shortest path

## Syntax

```python
Geometry.Edge.NodeShortestPath(crFirstNode, crSecondNode, iEnableBreakFace=1)
```

Macro: {ref}`Macro-Geometry-CreateEdgeBy2NodeShortestPath`

Ribbon: {menuselection}`Geometry --> Edge --> NodeShortestPath`

## Inputs

**`crFirstNode`**
: A _Cursor_ specifying the first node. This is a required input.

**`crSecondNode`**
: A _Cursor_ specifying the second node. This is a required input.

**`iEnableBreakFace`**
: An _Integer_ specifying the enable break face. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.NodeShortestPath(crFirstNode, crSecondNode, iEnableBreakFace=1)
```
