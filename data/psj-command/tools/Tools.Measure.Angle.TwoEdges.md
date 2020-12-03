```{module} Tools.Measure.Angle.TwoEdges()
:synopsis: Measure the angle created by 2 edges.
```

(Tools.Measure.Angle.TwoEdges)=

# Tools.Measure.Angle.TwoEdges

## Description

Measure the angle created by 2 edges.

## Syntax

```python
Tools.Measure.Angle.TwoEdges(crEdge1, crEdge2, strTarget="Angle", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleBy2Edges`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> TwoEdges`

## Inputs

**`crEdge1`**
: A _Cursor_ specifying the edge1. This is a required input.

**`crEdge2`**
: A _Cursor_ specifying the edge2. This is a required input.

**`strTarget`**
: A _String_ specifying the target. The default value is "Angle".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.TwoEdges(crEdge1, crEdge2, strTarget="Angle", iPrecision=6)
```
