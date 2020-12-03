```{module} HexModeling.SolidElemInterface()
:synopsis: make solid element interface
```

(HexModeling.SolidElemInterface)=

# HexModeling.SolidElemInterface

## Description

make solid element interface

## Syntax

```python
HexModeling.SolidElemInterface(crlFace=[], bFlip=False, crlElms=[])
```

Macro: {ref}`Macro-HexModeling-SolidElemInterface`

Ribbon: {menuselection}`HexModeling --> SolidElemInterface`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bFlip`**
: A _Boolean_ specifying the flip. The default value is False.

**`crlElms`**
: A _Cursor List_ specifying the elms. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.SolidElemInterface(crlFace=[], bFlip=False, crlElms=[])
```
