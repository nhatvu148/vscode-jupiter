```{module} MidPlaneEdit.ExtendFace.CylinderFace()
:synopsis: project an edge to face to get a new edge
```

(MidPlaneEdit.ExtendFace.CylinderFace)=

# MidPlaneEdit.ExtendFace.CylinderFace

## Description

project an edge to face to get a new edge

## Syntax

```python
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```

Macro: {ref}`Macro-MidPlaneEdit-ExtendFaceCylinderFace`

Ribbon: {menuselection}`MidPlaneEdit --> ExtendFace --> CylinderFace`

## Inputs

**`crlExtFace`**
: A _Cursor List_ specifying the extend face. The default value is [].

**`crRefFace`**
: A _Cursor_ specifying the reference face. The default value is None.

**`crEdge`**
: A _Cursor_ specifying the edge. The default value is None.

**`iExtendType`**
: An _Integer_ specifying the extend type. The default value is 1.

**`iFaceType`**
: An _Integer_ specifying the face type. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`dParaAngleOffset`**
: A _Double_ specifying the parameter angle offset. The default value is 0.0.

**`dParaArcLength`**
: A _Double_ specifying the parameter arc length. The default value is 0.0.

**`dParaZxy`**
: A _Double_ specifying the parameter zxy. The default value is 0.0.

**`iAxisPlane`**
: An _Integer_ specifying the axis plane. The default value is 0.

**`iParaArcNodesNum`**
: An _Integer_ specifying the parameter arc nodes number. The default value is 0.

**`dOffLength`**
: A _Double_ specifying the off length. The default value is 0.0.

**`crlSelExtendedFace`**
: A _Cursor List_ specifying the selection extended face. The default value is [].

**`crlSelRefFace`**
: A _Cursor List_ specifying the selection reference face. The default value is [].

**`dCoMag`**
: A _Double_ specifying the coordinate mag. The default value is 0.0.

**`iAxisSystem`**
: An _Integer_ specifying the axis system. The default value is 0.

**`iCoorSystem`**
: An _Integer_ specifying the coordinate system. The default value is 0.

**`iCoX`**
: An _Integer_ specifying the coordinate x. The default value is 0.

**`iCoY`**
: An _Integer_ specifying the coordinate y. The default value is 0.

**`iCoZ`**
: An _Integer_ specifying the coordinate z. The default value is 0.

**`bOtherSameAsFaceNormal`**
: A _Boolean_ specifying the other same as face normal. The default value is False.

**`dOtherArcNodesNum`**
: A _Double_ specifying the other arc nodes number. The default value is 0.0.

**`dOtherArcRadius`**
: A _Double_ specifying the other arc radius. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```
