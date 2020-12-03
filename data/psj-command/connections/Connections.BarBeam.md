```{module} Connections.BarBeam()
:synopsis: create Connections Bar or Beam
```

(Connections.BarBeam)=

# Connections.BarBeam

## Description

create Connections Bar or Beam

## Syntax

```python
Connections.BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTarget=[], crlSlaveTarget=[])
```

Macro: {ref}`Macro-Connections-ConnectionBarBeam`

Ribbon: {menuselection}`Connections --> BarBeam`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`iEType`**
: An _Integer_ specifying the e type. The default value is 10.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

**`crProp`**
: A _Cursor_ specifying the property. The default value is None.

**`dlOrient`**
: A _Double List_ specifying the orient. The default value is [].

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTarget=[], crlSlaveTarget=[])
```
