```{module} Tools.Measure.Angle.TwoAxis()
:synopsis: Measure the angle created by 2 Axis.
```

(Tools.Measure.Angle.TwoAxis)=

# Tools.Measure.Angle.TwoAxis

## Description

Measure the angle created by 2 Axis.

## Syntax

```python
Tools.Measure.Angle.TwoAxis(dlXyz1=[0, 0, 0], dlXyz2=[0, 0, 0], strTarget="Angle", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleBy2Axis`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> TwoAxis`

## Inputs

**`dlXyz1`**
: A _Double List_ specifying the xyz1. The default value is [0, 0, 0].

**`dlXyz2`**
: A _Double List_ specifying the xyz2. The default value is [0, 0, 0].

**`strTarget`**
: A _String_ specifying the target. The default value is "Angle".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.TwoAxis(dlXyz1=[0, 0, 0], dlXyz2=[0, 0, 0], strTarget="Angle", iPrecision=6)
```
