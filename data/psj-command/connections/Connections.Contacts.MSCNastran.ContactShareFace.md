```{module} Connections.Contacts.MSCNastran.ContactShareFace()
:synopsis: create contacts of MSC Nastran Contact Share Face
```

(Connections.Contacts.MSCNastran.ContactShareFace)=

# Connections.Contacts.MSCNastran.ContactShareFace

## Description

create contacts of MSC Nastran Contact Share Face

## Syntax

```python
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```

Macro: {ref}`Macro-Connections-LbcContactShareFaceMSCNastranCr`

Ribbon: {menuselection}`Connections --> Contacts --> MSCNastran --> ContactShareFace`

## Inputs

**`crlShareFace`**
: A _Cursor List_ specifying the share face. The default value is [].

**`strName`**
: A _String_ specifying the name. The default value is "".

**`nastranContact`**
: A _NASTRAN_CONTACT_ specifying the contact. The default value is NASTRAN_CONTACT().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 65280.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 3.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```
