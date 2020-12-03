```{module} Connections.SpringsDampers.Damper.AnyEntities11DoFS()
:synopsis: Create Damper Connection
```

(Connections.SpringsDampers.Damper.AnyEntities11DoFS)=

# Connections.SpringsDampers.Damper.AnyEntities11DoFS

## Description

Create Damper Connection

## Syntax

```python
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```

Macro: {ref}`Macro-Connections-Damper`

Ribbon: {menuselection}`Connections --> SpringsDampers --> Damper --> AnyEntities11DoFS`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. This is a required input.

**`strName`**
: A _String_ specifying the name. This is a required input.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. This is a required input.

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. This is a required input.

**`crCoordSys`**
: A _Cursor_ specifying the coordinate system. The default value is None.

**`iGround`**
: An _Integer_ specifying the ground. The default value is 0.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.0.

**`vecTDamper`**
: A _Vector_ specifying the t damper. The default value is [0, 0, 0].

**`vecRDamper`**
: A _Vector_ specifying the r damper. The default value is [0, 0, 0].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bUpdateDispCS`**
: A _Boolean_ specifying the update displacement coordinate system. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)
```
