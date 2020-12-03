```{module} Connections.Contacts.CheckPattern()
:synopsis: check contact Pattern
```

(Connections.Contacts.CheckPattern)=

# Connections.Contacts.CheckPattern

## Description

check contact Pattern

## Syntax

```python
Connections.Contacts.CheckPattern(crlPart=[], bShowMismatch=False, bShowMatch=True, dTol=0.01)
```

Macro: {ref}`Macro-Connections-CheckPattern`

Ribbon: {menuselection}`Connections --> Contacts --> CheckPattern`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bShowMismatch`**
: A _Boolean_ specifying the show mismatch. The default value is False.

**`bShowMatch`**
: A _Boolean_ specifying the show match. The default value is True.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 0.01.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.CheckPattern(crlPart=[], bShowMismatch=False, bShowMatch=True, dTol=0.01)
```
