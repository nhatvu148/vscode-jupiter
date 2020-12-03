```{module} Connections.Contacts.MSCNastran.ManualGroup()
:synopsis: create contacts of MSC Nastran
```

(Connections.Contacts.MSCNastran.ManualGroup)=

# Connections.Contacts.MSCNastran.ManualGroup

## Description

create contacts of MSC Nastran

## Syntax

```python
Connections.Contacts.MSCNastran.ManualGroup(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```

Macro: {ref}`Macro-Connections-ContactMSCNastran`

Ribbon: {menuselection}`Connections --> Contacts --> MSCNastran --> ManualGroup`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`nastranContact`**
: A _NASTRAN_CONTACT_ specifying the contact. The default value is NASTRAN_CONTACT().

**`crplTarget`**
: A _Cursor Pair List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 65280.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.MSCNastran.ManualGroup(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
