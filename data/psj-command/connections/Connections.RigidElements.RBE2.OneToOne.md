```{module} Connections.RigidElements.RBE2.OneToOne()
:synopsis: create RBE2
```

(Connections.RigidElements.RBE2.OneToOne)=

# Connections.RigidElements.RBE2.OneToOne

## Description

create RBE2

## Syntax

```python
Connections.RigidElements.RBE2.OneToOne(iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```

Macro: {ref}`Macro-Connections-RBE2OneToOne`

Ribbon: {menuselection}`Connections --> RigidElements --> RBE2 --> OneToOne`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 17.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`iEType`**
: An _Integer_ specifying the e type. The default value is 2.

**`strName`**
: A _String_ specifying the name. The default value is "RBE2_1".

**`crCoordSys`**
: A _Cursor_ specifying the coordinate system. The default value is None.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.0.

**`iUlDOFs`**
: An _Integer_ specifying the ul d o fs. The default value is 63.

**`dlVirtualNodePos`**
: A _Double List_ specifying the virtual node position. The default value is [0, 0, 0].

**`iSurfaceDef`**
: An _Integer_ specifying the surface definition. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iEnableUpdateDispCS`**
: An _Integer_ specifying the enable update displacement coordinate system. The default value is 1.

**`iEnableCornerOnly`**
: An _Integer_ specifying the enable corner only. The default value is 0.

**`iEnableCheckDulplicate`**
: An _Integer_ specifying the enable check dulplicate. The default value is 1.

**`iDuplicateMode`**
: An _Integer_ specifying the duplicate mode. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.RigidElements.RBE2.OneToOne(iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```
