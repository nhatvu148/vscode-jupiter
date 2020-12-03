```{module} Geometry.Edge.PlanarLine()
:synopsis: Imprint Planar Line
```

(Geometry.Edge.PlanarLine)=

# Geometry.Edge.PlanarLine

## Description

Imprint Planar Line

## Syntax

```python
Geometry.Edge.PlanarLine(veclPosition, crlTargetFace, crLocalCoord=None, iType=0, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintPlannarLineS`

Ribbon: {menuselection}`Geometry --> Edge --> PlanarLine`

## Inputs

**`veclPosition`**
: A _Vector List_ specifying the position. This is a required input.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. This is a required input.

**`crLocalCoord`**
: A _Cursor_ specifying the local coordinate. The default value is None.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.PlanarLine(veclPosition, crlTargetFace, crLocalCoord=None, iType=0, bBreakFace=True)
```
