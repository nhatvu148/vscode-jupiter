```{module} Tools.Measure.Distance.TwoPoints()
:synopsis: measure distance 2 points
```

(Tools.Measure.Distance.TwoPoints)=

# Tools.Measure.Distance.TwoPoints

## Description

measure distance 2 points

## Syntax

```python
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```

Macro: {ref}`Macro-Tools-MeasureDistanceBy2Points`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> TwoPoints`

## Inputs

**`posPoint1`**
: A _Position_ specifying the point1. The default value is [0,0,0].

**`posPoint2`**
: A _Position_ specifying the point2. The default value is [0,0,0].

**`strTarget`**
: A _String_ specifying the target. The default value is "ALL".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

**`crCoordinateSystem`**
: A _Cursor_ specifying the coordinate system. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
