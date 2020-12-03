```{module} Geometry.Transform.Translation()
:synopsis: Translate the selected Part.
```

(Geometry.Transform.Translation)=

# Geometry.Transform.Translation

## Description

Translate the selected Part.

## Syntax

```python
Geometry.Transform.Translation(crlPart=[], poslTranslates=[], crCoord=None, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1)
```

Macro: {ref}`Macro-Geometry-TranslateBody`

Ribbon: {menuselection}`Geometry --> Transform --> Translation`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`poslTranslates`**
: A _Position List_ specifying the translates. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

**`iCopyCount`**
: An _Integer_ specifying the copy count. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.Translation(crlPart=[], poslTranslates=[], crCoord=None, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1)
```
