```{module} Connections.Contacts.ADVC.ContactClearance()
:synopsis: contact clearance for ADVC contact
```

(Connections.Contacts.ADVC.ContactClearance)=

# Connections.Contacts.ADVC.ContactClearance

## Description

contact clearance for ADVC contact

## Syntax

```python
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTarget, crEdit=None)
```

Macro: {ref}`Macro-Connections-ContactClearance`

Ribbon: {menuselection}`Connections --> Contacts --> ADVC --> ContactClearance`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`dClearanceVal`**
: A _Double_ specifying the clearance value. This is a required input.

**`iLocalUnit`**
: An _Integer_ specifying the local unit. This is a required input.

**`iSolverType`**
: An _Integer_ specifying the solver type. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTarget, crEdit=None)
```
