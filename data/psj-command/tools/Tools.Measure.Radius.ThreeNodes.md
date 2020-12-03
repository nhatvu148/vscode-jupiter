```{module} Tools.Measure.Radius.ThreeNodes()
:synopsis: Measure Radius MeasureRadiusBy3Nodes
```

(Tools.Measure.Radius.ThreeNodes)=

# Tools.Measure.Radius.ThreeNodes

## Description

Measure Radius MeasureRadiusBy3Nodes

## Syntax

```python
Tools.Measure.Radius.ThreeNodes(crNode13, crNode23, crNode33, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureRadiusBy3Nodes`

Ribbon: {menuselection}`Tools --> Measure --> Radius --> ThreeNodes`

## Inputs

**`crNode13`**
: A _Cursor_ specifying the node13. This is a required input.

**`crNode23`**
: A _Cursor_ specifying the node23. This is a required input.

**`crNode33`**
: A _Cursor_ specifying the node33. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Radius.ThreeNodes(crNode13, crNode23, crNode33, iPrecision=6)
```
