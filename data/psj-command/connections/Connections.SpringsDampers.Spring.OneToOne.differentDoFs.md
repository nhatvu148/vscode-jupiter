```{module} Connections.SpringsDampers.Spring.OneToOne.differentDoFs()
:synopsis: Spring connection One to One different DOFs
```

(Connections.SpringsDampers.Spring.OneToOne.differentDoFs)=

# Connections.SpringsDampers.Spring.OneToOne.differentDoFs

## Description

Spring connection One to One different DOFs

## Syntax

```python
Connections.SpringsDampers.Spring.OneToOne.differentDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```

Macro: {ref}`Macro-Connections-SpringOneToOneDOFs`

Ribbon: {menuselection}`Connections --> SpringsDampers --> Spring --> OneToOne --> differentDoFs`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`strName`**
: A _String_ specifying the name. The default value is "SPRING".

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`crCoordSys`**
: A _Cursor_ specifying the coordinate system. The default value is None.

**`iSpringType`**
: An _Integer_ specifying the spring type. The default value is 0.

**`iGround`**
: An _Integer_ specifying the ground. The default value is 0.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.0.

**`iDirection`**
: An _Integer_ specifying the direction. The default value is 0.

**`iDistributeMode`**
: An _Integer_ specifying the distribute mode. The default value is 0.

**`iDof1`**
: An _Integer_ specifying the dof1. The default value is 0.

**`iDof2`**
: An _Integer_ specifying the dof2. The default value is 0.

**`dDampCoef`**
: A _Double_ specifying the damp coefficient . The default value is DFLT_DBL.

**`dStressCoef`**
: A _Double_ specifying the stress coefficient . The default value is DFLT_DBL.

**`posTStiffness`**
: A _Position_ specifying the t stiffness. The default value is [0,0,0].

**`posRStiffness`**
: A _Position_ specifying the r stiffness. The default value is [0,0,0].

**`bUpdateDispCS`**
: A _Boolean_ specifying the update displacement coordinate system. The default value is True.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.SpringsDampers.Spring.OneToOne.differentDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```
