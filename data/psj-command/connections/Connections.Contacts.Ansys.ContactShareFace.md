```{module} Connections.Contacts.Ansys.ContactShareFace()
:synopsis: create contact ansys Share Face
```

(Connections.Contacts.Ansys.ContactShareFace)=

# Connections.Contacts.Ansys.ContactShareFace

## Description

create contact ansys Share Face

## Syntax

```python
Connections.Contacts.Ansys.ContactShareFace(crlShareFace=[], strName="ContactAnsys_1", iMethod=3, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)
```

Macro: {ref}`Macro-Connections-LbcContactShareFaceANSYSCr`

Ribbon: {menuselection}`Connections --> Contacts --> Ansys --> ContactShareFace`

## Inputs

**`crlShareFace`**
: A _Cursor List_ specifying the share face. The default value is [].

**`strName`**
: A _String_ specifying the name. The default value is "ContactAnsys_1".

**`iMethod`**
: An _Integer_ specifying the method. The default value is 3.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iContactAlgorithm`**
: An _Integer_ specifying the contact algorithm. The default value is 0.

**`ansysContact`**
: A _ANSYS_CONTACT_ specifying the contact. The default value is ANSYS_CONTACT().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 16711680.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.Ansys.ContactShareFace(crlShareFace=[], strName="ContactAnsys_1", iMethod=3, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)
```
