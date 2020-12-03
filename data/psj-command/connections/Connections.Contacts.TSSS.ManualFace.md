```{module} Connections.Contacts.TSSS.ManualFace()
:synopsis: Create Contact TSSS Manual Face
```

(Connections.Contacts.TSSS.ManualFace)=

# Connections.Contacts.TSSS.ManualFace

## Description

Create Contact TSSS Manual Face

## Syntax

```python
Connections.Contacts.TSSS.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crEdit=None, iColor=0, iMethod=0)
```

Macro: {ref}`Macro-Connections-ContactManualFaceTSSS`

Ribbon: {menuselection}`Connections --> Contacts --> TSSS --> ManualFace`

## Inputs

**`crlFaceMaster`**
: A _Cursor List_ specifying the face master. The default value is [].

**`crlFaceSlave`**
: A _Cursor List_ specifying the face slave. The default value is [].

**`strName`**
: A _String_ specifying the name. The default value is "ContactTS_SS_1".

**`nastranContact`**
: A _NASTRAN_CONTACT_ specifying the contact. The default value is SUNSHINE_CONTACT().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.TSSS.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crEdit=None, iColor=0, iMethod=0)
```
