```{module} Geometry.Edge.ElementEdges()
:synopsis: Create Edge by element edges
```

(Geometry.Edge.ElementEdges)=

# Geometry.Edge.ElementEdges

## Description

Create Edge by element edges

## Syntax

```python
Geometry.Edge.ElementEdges(crplElemEdge, bBreakEdge=True)
```

Macro: {ref}`Macro-Geometry-CreateEdgeByElemEdge`

Ribbon: {menuselection}`Geometry --> Edge --> ElementEdges`

## Inputs

**`crplElemEdge`**
: A _Cursor Pair List_ specifying the element edge. This is a required input.

**`bBreakEdge`**
: A _Boolean_ specifying the break edge. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.ElementEdges(crplElemEdge, bBreakEdge=True)
```
