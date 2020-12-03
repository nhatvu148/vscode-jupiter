```{module} Tools.Measure.Angle.TwoElemEdges()
:synopsis:
```

(Tools.Measure.Angle.TwoElemEdges)=

# Tools.Measure.Angle.TwoElemEdges

## Description

## Syntax

```python
Tools.Measure.Angle.TwoElemEdges(crpElemEdge1, crpElemEdge2, strTarget="Angle", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleBy2ElemEdges`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> TwoElemEdges`

## Inputs

**`crpElemEdge1`**
: A _Cursor Pair_ specifying the element edge1. This is a required input.

**`crpElemEdge2`**
: A _Cursor Pair_ specifying the element edge2. This is a required input.

**`strTarget`**
: A _String_ specifying the target. The default value is "Angle".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.TwoElemEdges(crpElemEdge1, crpElemEdge2, strTarget="Angle", iPrecision=6)
```
