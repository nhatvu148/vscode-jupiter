```{module} Assemble.SeparateFaces.Solid()
:synopsis:
```

(Assemble.SeparateFaces.Solid)=

# Assemble.SeparateFaces.Solid

## Description

## Syntax

```python
Assemble.SeparateFaces.Solid(crlPart=[], crlFace=[], bCreateGroup=False)
```

Macro: {ref}`Macro-Assemble-ASMSeparateSolidCr`

Ribbon: {menuselection}`Assemble --> SeparateFaces --> Solid`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bCreateGroup`**
: A _Boolean_ specifying the create group. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.SeparateFaces.Solid(crlPart=[], crlFace=[], bCreateGroup=False)
```
