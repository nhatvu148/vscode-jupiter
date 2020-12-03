```{module} Geometry.Part.Sphere()
:synopsis: create Sphere part
```

(Geometry.Part.Sphere)=

# Geometry.Part.Sphere

## Description

create Sphere part

## Syntax

```python
Geometry.Part.Sphere(dlOrigin=[0, 0, 0], dRadius=0.005, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Sphere_1", iColorPart=7105764, crCoord=None)
```

Macro: {ref}`Macro-Geometry-CreateSphere`

Ribbon: {menuselection}`Geometry --> Part --> Sphere`

## Inputs

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0, 0, 0].

**`dRadius`**
: A _Double_ specifying the radius. The default value is 0.005.

**`iLatitudeNodeCnt`**
: An _Integer_ specifying the latitude node cnt. The default value is 20.

**`iLongitudeNodeCnt`**
: An _Integer_ specifying the longitude node cnt. The default value is 20.

**`strPartName`**
: A _String_ specifying the part name. The default value is "Sphere_1".

**`iColorPart`**
: An _Integer_ specifying the color part. The default value is 7105764.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Sphere(dlOrigin=[0, 0, 0], dRadius=0.005, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Sphere_1", iColorPart=7105764, crCoord=None)
```
