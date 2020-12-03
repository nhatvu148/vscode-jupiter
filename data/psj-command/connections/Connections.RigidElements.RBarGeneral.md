```{module} Connections.RigidElements.RBarGeneral()
:synopsis: Unknown Description
```

(Connections.RigidElements.RBarGeneral)=

# Connections.RigidElements.RBarGeneral

## Description

Unknown Description

## Syntax

```python
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR_CONNECTION(), crlMasterTarget=[], crlSlaveTarget=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Connections-RBar`

Ribbon: {menuselection}`Connections --> RigidElements --> RBarGeneral`

## Inputs

**`rbarConnection`**
: A _RBAR_CONNECTION_ specifying the connection. The default value is RBAR_CONNECTION().

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`iUlDOFs`**
: An _Integer_ specifying the ul d o fs. The default value is 0.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is DFLT_DBL.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.RigidElements.RBarGeneral(rbarConnection=RBAR_CONNECTION(), crlMasterTarget=[], crlSlaveTarget=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```
