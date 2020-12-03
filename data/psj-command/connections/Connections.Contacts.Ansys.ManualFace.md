```{module} Connections.Contacts.Ansys.ManualFace()
:synopsis: create contacts of Ansys Manual Face
```

(Connections.Contacts.Ansys.ManualFace)=

# Connections.Contacts.Ansys.ManualFace

## Description

create contacts of Ansys Manual Face

## Syntax

```python
Connections.Contacts.Ansys.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)
```

Macro: {ref}`Macro-Connections-LbcContactManualFaceAnsys`

Ribbon: {menuselection}`Connections --> Contacts --> Ansys --> ManualFace`

## Inputs

**`crlFaceMaster`**
: A _Cursor List_ specifying the face master. The default value is [].

**`crlFaceSlave`**
: A _Cursor List_ specifying the face slave. The default value is [].

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

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 16711680.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.Ansys.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)
```
