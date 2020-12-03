```{module} Connections.Contacts.TSSolver.ManualGroup()
:synopsis: Create TSSolver Contact
```

(Connections.Contacts.TSSolver.ManualGroup)=

# Connections.Contacts.TSSolver.ManualGroup

## Description

Create TSSolver Contact

## Syntax

```python
Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_1", tssolverContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0)
```

Macro: {ref}`Macro-Connections-LbcContactTSSolver_ManualGroup`

Ribbon: {menuselection}`Connections --> Contacts --> TSSolver --> ManualGroup`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ContactTSSolver_1".

**`tssolverContact`**
: A _TSSOLVER_CONTACT_ specifying the contact. The default value is TSSOLVER_CONTACT().

**`crplTarget`**
: A _Cursor Pair List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 16711680.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_1", tssolverContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0)
```
