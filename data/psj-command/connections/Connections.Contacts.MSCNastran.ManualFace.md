```{module} Connections.Contacts.MSCNastran.ManualFace()
:synopsis: create contacts of MSC Nastran Manual Face
```

(Connections.Contacts.MSCNastran.ManualFace)=

# Connections.Contacts.MSCNastran.ManualFace

## Description

create contacts of MSC Nastran Manual Face

## Syntax

```python
Connections.Contacts.MSCNastran.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactMSCNastran", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=0)
```

Macro: {ref}`Macro-Connections-LbcContactManualFaceMSCNastran`

Ribbon: {menuselection}`Connections --> Contacts --> MSCNastran --> ManualFace`

## Inputs

**`crlFaceMaster`**
: A _Cursor List_ specifying the face master. The default value is [].

**`crlFaceSlave`**
: A _Cursor List_ specifying the face slave. The default value is [].

**`strName`**
: A _String_ specifying the name. The default value is "ContactMSCNastran".

**`nastranContact`**
: A _NASTRAN_CONTACT_ specifying the contact. The default value is NASTRAN_CONTACT().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 65280.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.MSCNastran.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactMSCNastran", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=0)
```
