```{module} Connections.Contacts.MSCNastran.ContactTable()
:synopsis: create contacts of MSC Nastran Contact Table
```

(Connections.Contacts.MSCNastran.ContactTable)=

# Connections.Contacts.MSCNastran.ContactTable

## Description

create contacts of MSC Nastran Contact Table

## Syntax

```python
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```

Macro: {ref}`Macro-Connections-LbcContactTableMSCNastran`

Ribbon: {menuselection}`Connections --> Contacts --> MSCNastran --> ContactTable`

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
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
