```{module} Connections.Contacts.TSSS.ManualGroup()
:synopsis: Create Contact TSSS Manual FaceGroup
```

(Connections.Contacts.TSSS.ManualGroup)=

# Connections.Contacts.TSSS.ManualGroup

## Description

Create Contact TSSS Manual FaceGroup

## Syntax

```python
Connections.Contacts.TSSS.ManualGroup(strName="ContactTS_SS_1", tssolverContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)
```

Macro: {ref}`Macro-Connections-ContactTSSS`

Ribbon: {menuselection}`Connections --> Contacts --> TSSS --> ManualGroup`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ContactTS_SS_1".

**`tssolverContact`**
: A _TSSOLVER_CONTACT_ specifying the contact. The default value is SUNSHINE_CONTACT().

**`crplTarget`**
: A _Cursor Pair List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.TSSS.ManualGroup(strName="ContactTS_SS_1", tssolverContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)
```
