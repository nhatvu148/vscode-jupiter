```{module} Geometry.ShellAsm()
:synopsis: assemble the separated parts
```

(Geometry.ShellAsm)=

# Geometry.ShellAsm

## Description

assemble the separated parts

## Syntax

```python
Geometry.ShellAsm(crlPartK=[], crlFaceK=[], dTol=0.2, iElemType=0, bSkipTiny=False)
```

Macro: {ref}`Macro-Geometry-ShellAsm`

Ribbon: {menuselection}`Geometry --> ShellAsm`

## Inputs

**`crlPartK`**
: A _Cursor List_ specifying the part k. The default value is [].

**`crlFaceK`**
: A _Cursor List_ specifying the face k. The default value is [].

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 0.2.

**`iElemType`**
: An _Integer_ specifying the element type. The default value is 0.

**`bSkipTiny`**
: A _Boolean_ specifying the skip tiny. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.ShellAsm(crlPartK=[], crlFaceK=[], dTol=0.2, iElemType=0, bSkipTiny=False)
```
