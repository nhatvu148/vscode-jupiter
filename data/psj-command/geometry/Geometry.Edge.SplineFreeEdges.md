```{module} Geometry.Edge.SplineFreeEdges()
:synopsis: Create Edge by spline
```

(Geometry.Edge.SplineFreeEdges)=

# Geometry.Edge.SplineFreeEdges

## Description

Create Edge by spline

## Syntax

```python
Geometry.Edge.SplineFreeEdges(crlNode, iEnableArc=0, crPart=None, strBarName="")
```

Macro: {ref}`Macro-Geometry-CreateEdgeSpline`

Ribbon: {menuselection}`Geometry --> Edge --> SplineFreeEdges`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`iEnableArc`**
: An _Integer_ specifying the enable arc. The default value is 0.

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

**`strBarName`**
: A _String_ specifying the bar name. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.SplineFreeEdges(crlNode, iEnableArc=0, crPart=None, strBarName="")
```
