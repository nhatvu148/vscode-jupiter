```{module} Connections.Contacts.Ansys.ManualGroup()
:synopsis: create contact ansys Manual Group
```

(Connections.Contacts.Ansys.ManualGroup)=

# Connections.Contacts.Ansys.ManualGroup

## Description

create contact ansys Manual Group

## Syntax

```python
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```

Macro: {ref}`Macro-Connections-ContactAnsys`

Ribbon: {menuselection}`Connections --> Contacts --> Ansys --> ManualGroup`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ContactAnsys_1".

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iContactAlgorithm`**
: An _Integer_ specifying the contact algorithm. The default value is 0.

**`ansysContact`**
: A _ANSYS_CONTACT_ specifying the contact. The default value is ANSYS_CONTACT().

**`crplTarget`**
: A _Cursor Pair List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 16711680.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```
