```{module} Geometry.Part.Cylinder()
:synopsis: create cylinder part
```

(Geometry.Part.Cylinder)=

# Geometry.Part.Cylinder

## Description

create cylinder part

## Syntax

```python
Geometry.Part.Cylinder(dlOrigin=[0,0,0], dTopRadius=0.01, dBotRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None)
```

Macro: {ref}`Macro-Geometry-CreateCylinderFrustum`

Ribbon: {menuselection}`Geometry --> Part --> Cylinder`

## Inputs

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0,0,0].

**`dTopRadius`**
: A _Double_ specifying the top radius. The default value is 0.01.

**`dBotRadius`**
: A _Double_ specifying the bot radius. The default value is 0.01.

**`dHeight`**
: A _Double_ specifying the height. The default value is 0.01.

**`iCircleNodeCnt`**
: An _Integer_ specifying the circle node cnt. The default value is 36.

**`iAxisNodeCnt`**
: An _Integer_ specifying the axis node cnt. The default value is 10.

**`strName`**
: A _String_ specifying the name. The default value is "Cylinder_1".

**`iPartCol`**
: An _Integer_ specifying the part col. The default value is 7105764.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Cylinder(dlOrigin=[0,0,0], dTopRadius=0.01, dBotRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None)
```
