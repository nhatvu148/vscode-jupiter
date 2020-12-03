```{module} Properties.RigidBody()
:synopsis: assign properties rigid body
```

(Properties.RigidBody)=

# Properties.RigidBody

## Description

assign properties rigid body

## Syntax

```python
Properties.RigidBody(strName="RigidBody1", iId=1, iRefNodeId=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Properties-Property2DRigidBody`

Ribbon: {menuselection}`Properties --> RigidBody`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "RigidBody1".

**`iId`**
: An _Integer_ specifying the ID. The default value is 1.

**`iRefNodeId`**
: An _Integer_ specifying the reference node ID. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.RigidBody(strName="RigidBody1", iId=1, iRefNodeId=0, crlTarget=[], crEdit=None)
```
