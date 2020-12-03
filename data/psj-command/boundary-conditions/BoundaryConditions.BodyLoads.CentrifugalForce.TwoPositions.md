```{module} BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions()
:synopsis: create centrifugal force
```

(BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions)=

# BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions

## Description

create centrifugal force

## Syntax

```python
BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(strName="CentrifugalForce1", dFBasePoint1=0.0, dFBasePoint2=0.0, dFBasePoint3=0.0, dFTipPoint1=0.0, dFTipPoint2=0.0, dFTipPoint3=0.0, dFVelocity=0.0, dFAcceleration=0.0, iVelocityUnit=0, iAccelerationUnit=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-CentrifugalForce2Positions`

Ribbon: {menuselection}`BoundaryConditions --> BodyLoads --> CentrifugalForce --> TwoPositions`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CentrifugalForce1".

**`dFBasePoint1`**
: A _Double_ specifying the base point1. The default value is 0.0.

**`dFBasePoint2`**
: A _Double_ specifying the base point2. The default value is 0.0.

**`dFBasePoint3`**
: A _Double_ specifying the base point3. The default value is 0.0.

**`dFTipPoint1`**
: A _Double_ specifying the tip point1. The default value is 0.0.

**`dFTipPoint2`**
: A _Double_ specifying the tip point2. The default value is 0.0.

**`dFTipPoint3`**
: A _Double_ specifying the tip point3. The default value is 0.0.

**`dFVelocity`**
: A _Double_ specifying the velocity. The default value is 0.0.

**`dFAcceleration`**
: A _Double_ specifying the acceleration. The default value is 0.0.

**`iVelocityUnit`**
: An _Integer_ specifying the velocity unit. The default value is 0.

**`iAccelerationUnit`**
: An _Integer_ specifying the acceleration unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(strName="CentrifugalForce1", dFBasePoint1=0.0, dFBasePoint2=0.0, dFBasePoint3=0.0, dFTipPoint1=0.0, dFTipPoint2=0.0, dFTipPoint3=0.0, dFVelocity=0.0, dFAcceleration=0.0, iVelocityUnit=0, iAccelerationUnit=0, crlTarget=[], crEdit=None)
```
