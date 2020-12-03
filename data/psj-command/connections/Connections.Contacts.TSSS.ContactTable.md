```{module} Connections.Contacts.TSSS.ContactTable()
:synopsis: Create Contact TSSS Manual FaceGroup
```

(Connections.Contacts.TSSS.ContactTable)=

# Connections.Contacts.TSSS.ContactTable

## Description

Create Contact TSSS Manual FaceGroup

## Syntax

```python
Connections.Contacts.TSSS.ContactTable(strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)
```

Macro: {ref}`Macro-Connections-ContactTSSS_ContactTable`

Ribbon: {menuselection}`Connections --> Contacts --> TSSS --> ContactTable`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ContactTS_SS_1".

**`nastranContact`**
: A _NASTRAN_CONTACT_ specifying the contact. The default value is SUNSHINE_CONTACT().

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
Connections.Contacts.TSSS.ContactTable(strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)
```
