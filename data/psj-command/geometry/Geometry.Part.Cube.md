```{module} Geometry.Part.Cube()
:synopsis: create cube part
```

(Geometry.Part.Cube)=

# Geometry.Part.Cube

## Description

create cube part

## Syntax

```python
Geometry.Part.Cube(dlOrigin=[0, 0, 0], dlLength=[0.01, 0.01, 0.01], ilNodeCnt=[10, 10, 10], strPartName="Cube_1", iColorPart=7105764, crCoord=None)
```

Macro: {ref}`Macro-Geometry-CreateCube`

Ribbon: {menuselection}`Geometry --> Part --> Cube`

## Inputs

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0, 0, 0].

**`dlLength`**
: A _Double List_ specifying the length. The default value is [0.01, 0.01, 0.01].

**`ilNodeCnt`**
: A _Integer List_ specifying the node cnt. The default value is [10, 10, 10].

**`strPartName`**
: A _String_ specifying the part name. The default value is "Cube_1".

**`iColorPart`**
: An _Integer_ specifying the color part. The default value is 7105764.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Cube(dlOrigin=[0, 0, 0], dlLength=[0.01, 0.01, 0.01], ilNodeCnt=[10, 10, 10], strPartName="Cube_1", iColorPart=7105764, crCoord=None)
```
