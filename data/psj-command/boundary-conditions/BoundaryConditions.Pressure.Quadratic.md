```{module} BoundaryConditions.Pressure.Quadratic()
:synopsis: Create Pressure quadratic
```

(BoundaryConditions.Pressure.Quadratic)=

# BoundaryConditions.Pressure.Quadratic

## Description

Create Pressure quadratic

## Syntax

```python
BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-PressureQuadratic`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> Quadratic`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PressureQuadratic1".

**`dA`**
: A _Double_ specifying the a. The default value is 0.0.

**`dB`**
: A _Double_ specifying the . The default value is 0.0.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dAngleRange`**
: A _Double_ specifying the angle range. The default value is 0.0.

**`iPressureDirectionMode`**
: An _Integer_ specifying the pressure direction mode. The default value is 0.

**`dlPressureDirection`**
: A _Double List_ specifying the pressure direction. The default value is [0.0,0.0,0.0].

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTarget=[], crEdit=None)
```
