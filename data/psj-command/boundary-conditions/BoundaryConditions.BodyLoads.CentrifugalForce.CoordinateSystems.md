```{module} BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems()
:synopsis: create centrifugal force by coordinate system
```

(BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems)=

# BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems

## Description

create centrifugal force by coordinate system

## Syntax

```python
BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(strName="CentrifugalForce1", dFVelocity=DFLT_DBL, dFAcceleration=DFLT_DBL, iAxisDirection=0, iVelocityUnit=0, iAccelerationUnit=0, crCurCoord=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-CentrifugalForceCoordinateSystem`

Ribbon: {menuselection}`BoundaryConditions --> BodyLoads --> CentrifugalForce --> CoordinateSystems`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CentrifugalForce1".

**`dFVelocity`**
: A _Double_ specifying the velocity. The default value is DFLT_DBL.

**`dFAcceleration`**
: A _Double_ specifying the acceleration. The default value is DFLT_DBL.

**`iAxisDirection`**
: An _Integer_ specifying the axis direction. The default value is 0.

**`iVelocityUnit`**
: An _Integer_ specifying the velocity unit. The default value is 0.

**`iAccelerationUnit`**
: An _Integer_ specifying the acceleration unit. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(strName="CentrifugalForce1", dFVelocity=DFLT_DBL, dFAcceleration=DFLT_DBL, iAxisDirection=0, iVelocityUnit=0, iAccelerationUnit=0, crCurCoord=None, crlTarget=[], crEdit=None)
```
