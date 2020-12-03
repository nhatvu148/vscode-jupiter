```{module} Geometry.Part.Wedge()
:synopsis: Create Wedge Body
```

(Geometry.Part.Wedge)=

# Geometry.Part.Wedge

## Description

Create Wedge Body

## Syntax

```python
Geometry.Part.Wedge(vecOrigin=[0.0, 0.0, 0.0], vecLength=[0.01, 0.01, 0.01], vecNodeCount=[10, 10, 10], strPartName="Wedge_1", iPartColor=7105764, crCoordinate=None)
```

Macro: {ref}`Macro-Geometry-CreateWedge`

Ribbon: {menuselection}`Geometry --> Part --> Wedge`

## Inputs

**`vecOrigin`**
: A _Vector_ specifying the original. The default value is [0.0, 0.0, 0.0].

**`vecLength`**
: A _Vector_ specifying the length. The default value is [0.01, 0.01, 0.01].

**`vecNodeCount`**
: A _Vector_ specifying the node count. The default value is [10, 10, 10].

**`strPartName`**
: A _String_ specifying the part name. The default value is "Wedge_1".

**`iPartColor`**
: An _Integer_ specifying the part color. The default value is 7105764.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Wedge(vecOrigin=[0.0, 0.0, 0.0], vecLength=[0.01, 0.01, 0.01], vecNodeCount=[10, 10, 10], strPartName="Wedge_1", iPartColor=7105764, crCoordinate=None)
```
