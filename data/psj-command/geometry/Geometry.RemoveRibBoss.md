```{module} Geometry.RemoveRibBoss()
:synopsis:
```

(Geometry.RemoveRibBoss)=

# Geometry.RemoveRibBoss

## Description

## Syntax

```python
Geometry.RemoveRibBoss(crlFace, dGradiation=1.0, iContinuity=1)
```

Macro: {ref}`Macro-Geometry-Remove_Rib_Boss`

Ribbon: {menuselection}`Geometry --> RemoveRibBoss`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`dGradiation`**
: A _Double_ specifying the gradiation. The default value is 1.0.

**`iContinuity`**
: An _Integer_ specifying the continuity. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.RemoveRibBoss(crlFace, dGradiation=1.0, iContinuity=1)
```
