```{module} Connections.Connector()
:synopsis: create Connector
```

(Connections.Connector)=

# Connections.Connector

## Description

create Connector

## Syntax

```python
Connections.Connector(strName="", iMethod=1, iConnectType=0, iRefNode=0, iElemCs=0, crLocalCS=None, crlElasticity=[], crlDamp=[], crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Connections-Connector`

Ribbon: {menuselection}`Connections --> Connector`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

**`iConnectType`**
: An _Integer_ specifying the connect type. The default value is 0.

**`iRefNode`**
: An _Integer_ specifying the reference node. The default value is 0.

**`iElemCs`**
: An _Integer_ specifying the element cs. The default value is 0.

**`crLocalCS`**
: A _Cursor_ specifying the local coordinate system. The default value is None.

**`crlElasticity`**
: A _Cursor List_ specifying the elasticity. The default value is [].

**`crlDamp`**
: A _Cursor List_ specifying the damp. The default value is [].

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
Connections.Connector(strName="", iMethod=1, iConnectType=0, iRefNode=0, iElemCs=0, crLocalCS=None, crlElasticity=[], crlDamp=[], crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)
```
