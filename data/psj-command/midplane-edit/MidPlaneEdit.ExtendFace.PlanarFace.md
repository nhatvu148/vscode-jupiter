```{module} MidPlaneEdit.ExtendFace.PlanarFace()
:synopsis: Extend Face
```

(MidPlaneEdit.ExtendFace.PlanarFace)=

# MidPlaneEdit.ExtendFace.PlanarFace

## Description

Extend Face

## Syntax

```python
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```

Macro: {ref}`Macro-MidPlaneEdit-MidplaneExtendPlane`

Ribbon: {menuselection}`MidPlaneEdit --> ExtendFace --> PlanarFace`

## Inputs

**`bIType`**
: A _Boolean_ specifying the type. The default value is False.

**`crExtFace`**
: A _Cursor_ specifying the extend face. The default value is None.

**`crRefFace`**
: A _Cursor_ specifying the reference face. The default value is None.

**`crEdge`**
: A _Cursor_ specifying the edge. The default value is None.

**`iFaceType`**
: An _Integer_ specifying the face type. The default value is 0.

**`iExtendType`**
: An _Integer_ specifying the extend type. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`dParaZxy`**
: A _Double_ specifying the parameter zxy. The default value is 0.

**`iAxisPlane`**
: An _Integer_ specifying the axis plane. The default value is 0.

**`iParaArcNodesNum`**
: An _Integer_ specifying the parameter arc nodes number. The default value is 0.

**`dOffLength`**
: A _Double_ specifying the off length. The default value is 0.

**`dCoMag`**
: A _Double_ specifying the coordinate mag. The default value is 0.

**`iAxisSystem`**
: An _Integer_ specifying the axis system. The default value is 0.

**`iCoorSystem`**
: An _Integer_ specifying the coordinate system. The default value is 0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iCoX`**
: An _Integer_ specifying the coordinate x. The default value is 0.

**`iCoY`**
: An _Integer_ specifying the coordinate y. The default value is 0.

**`iCoZ`**
: An _Integer_ specifying the coordinate z. The default value is 0.

**`bOtherSameAsFaceNormal`**
: A _Boolean_ specifying the other same as face normal. The default value is False.

**`dOtherArcNodesNum`**
: A _Double_ specifying the other arc nodes number. The default value is 0.

**`dOtherArcRadius`**
: A _Double_ specifying the other arc radius. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```
