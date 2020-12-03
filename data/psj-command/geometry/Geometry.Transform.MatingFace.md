```{module} Geometry.Transform.MatingFace()
:synopsis: Transform MatingFace
```

(Geometry.Transform.MatingFace)=

# Geometry.Transform.MatingFace

## Description

Transform MatingFace

## Syntax

```python
Geometry.Transform.MatingFace(crlPart=[], crSrcFace=None, crDstFace=None, crSrcEdge=None, crDstEdge=None, crSrcNode=None, crDstNode=None, iFaceOpposite=0, dEdgeAngle=0, iEdgeOpposite=0, iAlignMethodType=0, iAdjustPointType=0, iAdjustProjectionType=0, dlAlignVector=[0, 0, 0], dlAdjustPoint=[0, 0, 0], dlAdjustVector=[0, 0, 0], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bIsPreview=False, crlCoordSyss=[])
```

Macro: {ref}`Macro-Geometry-TransMatingFace`

Ribbon: {menuselection}`Geometry --> Transform --> MatingFace`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crSrcFace`**
: A _Cursor_ specifying the source face. The default value is None.

**`crDstFace`**
: A _Cursor_ specifying the dst face. The default value is None.

**`crSrcEdge`**
: A _Cursor_ specifying the source edge. The default value is None.

**`crDstEdge`**
: A _Cursor_ specifying the dst edge. The default value is None.

**`crSrcNode`**
: A _Cursor_ specifying the source node. The default value is None.

**`crDstNode`**
: A _Cursor_ specifying the dst node. The default value is None.

**`iFaceOpposite`**
: An _Integer_ specifying the face opposite. The default value is 0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 0.

**`iEdgeOpposite`**
: An _Integer_ specifying the edge opposite. The default value is 0.

**`iAlignMethodType`**
: An _Integer_ specifying the align method type. The default value is 0.

**`iAdjustPointType`**
: An _Integer_ specifying the adjust point type. The default value is 0.

**`iAdjustProjectionType`**
: An _Integer_ specifying the adjust projection type. The default value is 0.

**`dlAlignVector`**
: A _Double List_ specifying the align vector. The default value is [0, 0, 0].

**`dlAdjustPoint`**
: A _Double List_ specifying the adjust point. The default value is [0, 0, 0].

**`dlAdjustVector`**
: A _Double List_ specifying the adjust vector. The default value is [0, 0, 0].

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

**`bIsPreview`**
: A _Boolean_ specifying the is preview. The default value is False.

**`crlCoordSyss`**
: A _Cursor List_ specifying the coordinate system. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.MatingFace(crlPart=[], crSrcFace=None, crDstFace=None, crSrcEdge=None, crDstEdge=None, crSrcNode=None, crDstNode=None, iFaceOpposite=0, dEdgeAngle=0, iEdgeOpposite=0, iAlignMethodType=0, iAdjustPointType=0, iAdjustProjectionType=0, dlAlignVector=[0, 0, 0], dlAdjustPoint=[0, 0, 0], dlAdjustVector=[0, 0, 0], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bIsPreview=False, crlCoordSyss=[])
```
