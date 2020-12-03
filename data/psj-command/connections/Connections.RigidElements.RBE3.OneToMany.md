```{module} Connections.RigidElements.RBE3.OneToMany()
:synopsis: Create RBE3
```

(Connections.RigidElements.RBE3.OneToMany)=

# Connections.RigidElements.RBE3.OneToMany

## Description

Create RBE3

## Syntax

```python
Connections.RigidElements.RBE3.OneToMany(iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```

Macro: {ref}`Macro-Connections-RBE3OneToMany`

Ribbon: {menuselection}`Connections --> RigidElements --> RBE3 --> OneToMany`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 16.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`listRbe3TermConnection`**
: A _RBE3TERM_CONNECTION List_ specifying the rbe3 term connection. The default value is [].

**`iTypeRBE3`**
: An _Integer_ specifying the type r e3. The default value is 3.

**`strName`**
: A _String_ specifying the name. The default value is "".

**`crCoordSys`**
: A _Cursor_ specifying the coordinate system. The default value is None.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.0.

**`dlVirtualNodePos`**
: A _Double List_ specifying the virtual node position. The default value is [0, 0, 0].

**`iSurfaceDef`**
: An _Integer_ specifying the surface definition. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iEnableUpdateDispCS`**
: An _Integer_ specifying the enable update displacement coordinate system. The default value is True.

**`iEnableCornerOnly`**
: An _Integer_ specifying the enable corner only. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.RigidElements.RBE3.OneToMany(iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)
```
