```{module} Tools.Measure.Radius.Edge()
:synopsis: Measure edge minimum radius
```

(Tools.Measure.Radius.Edge)=

# Tools.Measure.Radius.Edge

## Description

Measure edge minimum radius

## Syntax

```python
Tools.Measure.Radius.Edge(crEdge, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureRadiusByEdge`

Ribbon: {menuselection}`Tools --> Measure --> Radius --> Edge`

## Inputs

**`crEdge`**
: A _Cursor_ specifying the edge. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Radius.Edge(crEdge, iPrecision=6)
```
