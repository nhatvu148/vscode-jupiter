```{module} Geometry.Part.Torus()
:synopsis: create Torus part
```

(Geometry.Part.Torus)=

# Geometry.Part.Torus

## Description

create Torus part

## Syntax

```python
Geometry.Part.Torus(dlOrigin=[0, 0, 0], dInnerRadius=0.015, dRingRadius=0.02, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Torus_1", iColorPart=7105764, crCoord=None)
```

Macro: {ref}`Macro-Geometry-CreateTorus`

Ribbon: {menuselection}`Geometry --> Part --> Torus`

## Inputs

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0, 0, 0].

**`dInnerRadius`**
: A _Double_ specifying the inner radius. The default value is 0.015.

**`dRingRadius`**
: A _Double_ specifying the ring radius. The default value is 0.02.

**`iLatitudeNodeCnt`**
: An _Integer_ specifying the latitude node cnt. The default value is 20.

**`iLongitudeNodeCnt`**
: An _Integer_ specifying the longitude node cnt. The default value is 20.

**`strPartName`**
: A _String_ specifying the part name. The default value is "Torus_1".

**`iColorPart`**
: An _Integer_ specifying the color part. The default value is 7105764.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Torus(dlOrigin=[0, 0, 0], dInnerRadius=0.015, dRingRadius=0.02, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Torus_1", iColorPart=7105764, crCoord=None)
```
