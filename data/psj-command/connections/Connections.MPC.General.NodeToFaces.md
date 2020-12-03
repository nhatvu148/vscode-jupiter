```{module} Connections.MPC.General.NodeToFaces()
:synopsis: Unknown Description
```

(Connections.MPC.General.NodeToFaces)=

# Connections.MPC.General.NodeToFaces

## Description

Unknown Description

## Syntax

```python
Connections.MPC.General.NodeToFaces(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)
```

Macro: {ref}`Macro-Connections-Mpc`

Ribbon: {menuselection}`Connections --> MPC --> General --> NodeToFaces`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "MPC_1".

**`crlMaster`**
: A _Cursor List_ specifying the master. The default value is [].

**`crlSlave`**
: A _Cursor List_ specifying the slave. The default value is [].

**`listMpcConnection`**
: A _MPC_CONNECTION List_ specifying the mpc connection. The default value is [].

**`dSearchTol`**
: A _Double_ specifying the search tolerance. The default value is 0.0.

**`dValue`**
: A _Double_ specifying the value. The default value is 0.0.

**`iMPCType`**
: An _Integer_ specifying the MPC type. The default value is 0.

**`iSearchType`**
: An _Integer_ specifying the search type. The default value is 1.

**`iCoordSys`**
: An _Integer_ specifying the coordinate system. The default value is 0.

**`bUpdateDispCS`**
: A _Boolean_ specifying the update displacement coordinate system. The default value is True.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.MPC.General.NodeToFaces(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)
```
