```{module} MidPlane.AdjustThickness()
:synopsis: Adjust thickness of midplane
```

(MidPlane.AdjustThickness)=

# MidPlane.AdjustThickness

## Description

Adjust thickness of midplane

## Syntax

```python
MidPlane.AdjustThickness(crlPart=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```

Macro: {ref}`Macro-MidPlane-MidPlaneAdjustThickness`

Ribbon: {menuselection}`MidPlane --> AdjustThickness`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dRatio`**
: A _Double_ specifying the ratio. The default value is 1.0.

**`bAdjustFaceThick`**
: A _Boolean_ specifying the adjust face thickness. The default value is False.

**`bAdjustPropThick`**
: A _Boolean_ specifying the adjust property thickness. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlane.AdjustThickness(crlPart=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```
