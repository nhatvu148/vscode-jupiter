```{module} Connections.RigidElements.RBar.OneToOne()
:synopsis: create RBar
```

(Connections.RigidElements.RBar.OneToOne)=

# Connections.RigidElements.RBar.OneToOne

## Description

create RBar

## Syntax

```python
Connections.RigidElements.RBar.OneToOne(strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=17, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Connections-RBarOneToOne`

Ribbon: {menuselection}`Connections --> RigidElements --> RBar --> OneToOne`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "RBAR_1".

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

**`iMethod`**
: An _Integer_ specifying the method. The default value is 17.

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
Connections.RigidElements.RBar.OneToOne(strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=17, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)
```
