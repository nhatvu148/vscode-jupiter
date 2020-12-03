```{module} Connections.Pretension.Advc()
:synopsis: Create ADVC pretension
```

(Connections.Pretension.Advc)=

# Connections.Pretension.Advc

## Description

Create ADVC pretension

## Syntax

```python
Connections.Pretension.Advc(strName="PreTensionAdvc1", bFixedLength=False, crEnforcedVelocity=None, dDvalue=0.0, iDirUpdateType=0, dlVnormal=[0,0,0], dlCtrolNodePos=[0,0,0], iRefNodeId=0, crEdit=None, crlTarget=[])
```

Macro: {ref}`Macro-Connections-LbcPretensionAdvc`

Ribbon: {menuselection}`Connections --> Pretension --> Advc`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PreTensionAdvc1".

**`bFixedLength`**
: A _Boolean_ specifying the fixed length. The default value is False.

**`crEnforcedVelocity`**
: A _Cursor_ specifying the enforced velocity. The default value is None.

**`dDvalue`**
: A _Double_ specifying the value. The default value is 0.0.

**`iDirUpdateType`**
: An _Integer_ specifying the direction update type. The default value is 0.

**`dlVnormal`**
: A _Double List_ specifying the vnormal. The default value is [0,0,0].

**`dlCtrolNodePos`**
: A _Double List_ specifying the ctrol node position. The default value is [0,0,0].

**`iRefNodeId`**
: An _Integer_ specifying the reference node ID. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Pretension.Advc(strName="PreTensionAdvc1", bFixedLength=False, crEnforcedVelocity=None, dDvalue=0.0, iDirUpdateType=0, dlVnormal=[0,0,0], dlCtrolNodePos=[0,0,0], iRefNodeId=0, crEdit=None, crlTarget=[])
```
