```{module} Geometry.Edge.Spline()
:synopsis: Imprint a Spline on a face
```

(Geometry.Edge.Spline)=

# Geometry.Edge.Spline

## Description

Imprint a Spline on a face

## Syntax

```python
Geometry.Edge.Spline(veclAprroxiPositions, crlTargetFace, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-GeoImprintSplineS`

Ribbon: {menuselection}`Geometry --> Edge --> Spline`

## Inputs

**`veclAprroxiPositions`**
: A _Vector List_ specifying the aprroxi positions. This is a required input.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. This is a required input.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.Spline(veclAprroxiPositions, crlTargetFace, bBreakFace=True)
```
