```{module} BoundaryConditions.Force.NonlinearForce.NOLIN1()
:synopsis: Create Nonlinear Force of NOLIN1(Table)
```

(BoundaryConditions.Force.NonlinearForce.NOLIN1)=

# BoundaryConditions.Force.NonlinearForce.NOLIN1

## Description

Create Nonlinear Force of NOLIN1(Table)

## Syntax

```python
BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1_1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-LbcNolin1Table`

Ribbon: {menuselection}`BoundaryConditions --> Force --> NonlinearForce --> NOLIN1`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "NonlinearForce1_1".

**`dForceScale`**
: A _Double_ specifying the force scale. The default value is 0.0.

**`dMomentScale`**
: A _Double_ specifying the moment scale. The default value is 0.0.

**`iForcDir`**
: An _Integer_ specifying the forc direction. The default value is 0.

**`iForceDepends`**
: An _Integer_ specifying the force depends. The default value is 0.

**`iMomentDir`**
: An _Integer_ specifying the moment direction. The default value is 0.

**`iMomentDepends`**
: An _Integer_ specifying the moment depends. The default value is 0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crForceTable`**
: A _Cursor_ specifying the force table. The default value is None.

**`crMomentTable`**
: A _Cursor_ specifying the moment table. The default value is None.

**`crlMaster`**
: A _Cursor List_ specifying the master. The default value is [].

**`crlSlave`**
: A _Cursor List_ specifying the slave. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1_1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)
```
