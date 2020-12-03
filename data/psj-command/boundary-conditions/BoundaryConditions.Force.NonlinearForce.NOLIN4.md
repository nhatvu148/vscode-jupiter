```{module} BoundaryConditions.Force.NonlinearForce.NOLIN4()
:synopsis: create NOLIN4 nonlinear force
```

(BoundaryConditions.Force.NonlinearForce.NOLIN4)=

# BoundaryConditions.Force.NonlinearForce.NOLIN4

## Description

create NOLIN4 nonlinear force

## Syntax

```python
BoundaryConditions.Force.NonlinearForce.NOLIN4(strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-LbcNolin4Exp`

Ribbon: {menuselection}`BoundaryConditions --> Force --> NonlinearForce --> NOLIN4`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`dForceScale`**
: A _Double_ specifying the force scale. The default value is 0.0.

**`dMomentScale`**
: A _Double_ specifying the moment scale. The default value is 0.0.

**`dForcePowerA`**
: A _Double_ specifying the force power a. The default value is 0.0.

**`dMomentPowerA`**
: A _Double_ specifying the moment power a. The default value is 0.0.

**`iForcDir`**
: An _Integer_ specifying the forc direction. The default value is 0.

**`iForceDepends`**
: An _Integer_ specifying the force depends. The default value is 0.

**`iMomentDir`**
: An _Integer_ specifying the moment direction. The default value is 0.

**`iMomentDepends`**
: An _Integer_ specifying the moment depends. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.NonlinearForce.NOLIN4(strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)
```
