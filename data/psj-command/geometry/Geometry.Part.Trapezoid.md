```{module} Geometry.Part.Trapezoid()
:synopsis: Create trapezoid part
```

(Geometry.Part.Trapezoid)=

# Geometry.Part.Trapezoid

## Description

Create trapezoid part

## Syntax

```python
Geometry.Part.Trapezoid(dlOrigin=[0.0,0.0,0.0], dlLength=[0.01, 0.01, 0.01], dTopXLength=7.0, dRadius=0, ilNodeCnt=[10, 10, 10], strPartName="Trapezoid_1", iColorPart=7105764, crCoord=None)
```

Macro: {ref}`Macro-Geometry-CreateTrapezoid`

Ribbon: {menuselection}`Geometry --> Part --> Trapezoid`

## Inputs

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0.0,0.0,0.0].

**`dlLength`**
: A _Double List_ specifying the length. The default value is [0.01, 0.01, 0.01].

**`dTopXLength`**
: A _Double_ specifying the top x length. The default value is 7.0.

**`dRadius`**
: A _Double_ specifying the radius. The default value is 0.

**`ilNodeCnt`**
: A _Integer List_ specifying the node cnt. The default value is [10, 10, 10].

**`strPartName`**
: A _String_ specifying the part name. The default value is "Trapezoid_1".

**`iColorPart`**
: An _Integer_ specifying the color part. The default value is 7105764.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Trapezoid(dlOrigin=[0.0,0.0,0.0], dlLength=[0.01, 0.01, 0.01], dTopXLength=7.0, dRadius=0, ilNodeCnt=[10, 10, 10], strPartName="Trapezoid_1", iColorPart=7105764, crCoord=None)
```
