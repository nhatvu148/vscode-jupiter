```{module} Geometry.Edge.Angle()
:synopsis: create new adge by convert angle
```

(Geometry.Edge.Angle)=

# Geometry.Edge.Angle

## Description

create new adge by convert angle

## Syntax

```python
Geometry.Edge.Angle(crpPair, dAngle=135.0, bCurvature=False, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-CreateEdgeByElemEdgeAngle`

Ribbon: {menuselection}`Geometry --> Edge --> Angle`

## Inputs

**`crpPair`**
: A _Cursor Pair_ specifying the pair. This is a required input.

**`dAngle`**
: A _Double_ specifying the angle. The default value is 135.0.

**`bCurvature`**
: A _Boolean_ specifying the curvature. The default value is False.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.Angle(crpPair, dAngle=135.0, bCurvature=False, bBreakFace=True)
```
