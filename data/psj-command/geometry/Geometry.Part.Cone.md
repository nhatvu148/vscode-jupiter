```{module} Geometry.Part.Cone()
:synopsis: Create Cone Body
```

(Geometry.Part.Cone)=

# Geometry.Part.Cone

## Description

Create Cone Body

## Syntax

```python
Geometry.Part.Cone(dlOriginXyz=[0,0,0], dBottomRadius=0.01, dHeight=0.02, iCircleNodeCount=20, iAxisNodeCnt=20, strPartName="Cone_1", iPartColor=7105764, crCoordinate=None)
```

Macro: {ref}`Macro-Geometry-CreateCone`

Ribbon: {menuselection}`Geometry --> Part --> Cone`

## Inputs

**`dlOriginXyz`**
: A _Double List_ specifying the original xyz. The default value is [0,0,0].

**`dBottomRadius`**
: A _Double_ specifying the bottom radius. The default value is 0.01.

**`dHeight`**
: A _Double_ specifying the height. The default value is 0.02.

**`iCircleNodeCount`**
: An _Integer_ specifying the circle node count. The default value is 20.

**`iAxisNodeCnt`**
: An _Integer_ specifying the axis node cnt. The default value is 20.

**`strPartName`**
: A _String_ specifying the part name. The default value is "Cone_1".

**`iPartColor`**
: An _Integer_ specifying the part color. The default value is 7105764.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Cone(dlOriginXyz=[0,0,0], dBottomRadius=0.01, dHeight=0.02, iCircleNodeCount=20, iAxisNodeCnt=20, strPartName="Cone_1", iPartColor=7105764, crCoordinate=None)
```
