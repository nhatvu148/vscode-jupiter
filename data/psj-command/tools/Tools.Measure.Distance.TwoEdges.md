```{module} Tools.Measure.Distance.TwoEdges()
:synopsis: measure the distance of two edges
```

(Tools.Measure.Distance.TwoEdges)=

# Tools.Measure.Distance.TwoEdges

## Description

measure the distance of two edges

## Syntax

```python
Tools.Measure.Distance.TwoEdges(crEdge1, crEdge2, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceBy2Edges`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> TwoEdges`

## Inputs

**`crEdge1`**
: A _Cursor_ specifying the edge1. This is a required input.

**`crEdge2`**
: A _Cursor_ specifying the edge2. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.TwoEdges(crEdge1, crEdge2, iPrecision=6)
```
