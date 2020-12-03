```{module} BoundaryConditions.Pressure.FunctionLoadToCylinderSine()
:synopsis: Unknown Description
```

(BoundaryConditions.Pressure.FunctionLoadToCylinderSine)=

# BoundaryConditions.Pressure.FunctionLoadToCylinderSine

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-PressureSine`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> FunctionLoadToCylinderSine`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PressureSine1".

**`dA`**
: A _Double_ specifying the a. The default value is 0.0.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dAngleRange`**
: A _Double_ specifying the angle range. The default value is 0.0.

**`bDistributionAxis`**
: A _Boolean_ specifying the distribution axis. The default value is False.

**`iPressureDirectionMode`**
: An _Integer_ specifying the pressure direction mode. The default value is 0.

**`bIsTotalForceAdjustment`**
: A _Boolean_ specifying the is total force adjustment. The default value is False.

**`dTotalForce`**
: A _Double_ specifying the total force. The default value is 0.0.

**`vecPressureDirection`**
: A _Vector_ specifying the pressure direction. The default value is [0.0,0.0,0.0].

**`crCoordinateSystemForDirection`**
: A _Cursor_ specifying the coordinate system for direction. The default value is None.

**`bIsCornerNodesDistribution`**
: A _Boolean_ specifying the is corner nodes distribution. The default value is False.

**`strFormulaForA`**
: A _String_ specifying the formula for a. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTarget=[], crEdit=None)
```
