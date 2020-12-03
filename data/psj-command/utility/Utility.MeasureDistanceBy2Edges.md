```{module} Utility.MeasureDistanceBy2Edges()
:synopsis: Unknown Description
```

(Utility.MeasureDistanceBy2Edges)=

# Utility.MeasureDistanceBy2Edges

## Description

Unknown Description

## Syntax

```python
Utility.MeasureDistanceBy2Edges(crEdgeFirst, crEdgeLast, iPrecision=6)
```

Macro: {ref}`Macro-Utility-MeasureDistanceBy2Edges`

Ribbon: {menuselection}`Utility --> MeasureDistanceBy2Edges`

## Inputs

**`crEdgeFirst`**
: A _Cursor_ specifying the edge first. This is a required input.

**`crEdgeLast`**
: A _Cursor_ specifying the edge last. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Utility.MeasureDistanceBy2Edges(crEdgeFirst, crEdgeLast, iPrecision=6)
```
