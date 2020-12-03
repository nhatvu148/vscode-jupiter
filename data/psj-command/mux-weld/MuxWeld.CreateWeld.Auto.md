```{module} MuxWeld.CreateWeld.Auto()
:synopsis: Auto create weld
```

(MuxWeld.CreateWeld.Auto)=

# MuxWeld.CreateWeld.Auto

## Description

Auto create weld

## Syntax

```python
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTarget, crlSlaveTarget, iIconnectattributeCoordsys, crEdit)
```

Macro: {ref}`Macro-MuxWeld-ConnectionWeld`

Ribbon: {menuselection}`MuxWeld --> CreateWeld --> Auto`

## Inputs

**`iIconnectattributeMethod`**
: An _Integer_ specifying the iconnectattribute method. This is a required input.

**`strStrconnectattributeName`**
: A _String_ specifying the strconnectattribute name. This is a required input.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. This is a required input.

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. This is a required input.

**`iIconnectattributeCoordsys`**
: An _Integer_ specifying the iconnectattribute coordsys. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTarget, crlSlaveTarget, iIconnectattributeCoordsys, crEdit)
```
