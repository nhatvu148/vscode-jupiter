```{module} HexModeling.BallHexa()
:synopsis: hexa modeling ball hexa
```

(HexModeling.BallHexa)=

# HexModeling.BallHexa

## Description

hexa modeling ball hexa

## Syntax

```python
HexModeling.BallHexa(crPart, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1")
```

Macro: {ref}`Macro-HexModeling-HexModelingBallHexa`

Ribbon: {menuselection}`HexModeling --> BallHexa`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`vecCenter`**
: A _Vector_ specifying the center. The default value is [0.0,0.0,0.0].

**`dRadius`**
: A _Double_ specifying the radius. The default value is 5.0.

**`dMeshSize`**
: A _Double_ specifying the mesh size. The default value is 0.5.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iLayer`**
: An _Integer_ specifying the layer. The default value is 3.

**`bMakeCenterNode`**
: A _Boolean_ specifying the make center node. The default value is True.

**`strPartName`**
: A _String_ specifying the part name. The default value is "HexBall_1".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.BallHexa(crPart, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1")
```
