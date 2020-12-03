```{module} Test.Connection.RRod()
:synopsis: create RRod
```

(Test.Connection.RRod)=

# Test.Connection.RRod

## Description

create RRod

## Syntax

```python
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTarget=[], crlSlaveTarget=[])
```

Macro: {ref}`Macro-Test-ConnRRod`

Ribbon: {menuselection}`Test --> Connection --> RRod`

## Inputs

**`rbarConnection`**
: A _RBAR_CONNECTION_ specifying the connection. The default value is RBAR_CONNECTION().

**`iUlDOFs`**
: An _Integer_ specifying the ul d o fs. The default value is 1.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 0.0.

**`crlMasterTarget`**
: A _Cursor List_ specifying the master target. The default value is [].

**`crlSlaveTarget`**
: A _Cursor List_ specifying the slave target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTarget=[], crlSlaveTarget=[])
```
