```{module} MidPlane.CreateThickProps()
:synopsis: create thickness properties for mid-plane
```

(MidPlane.CreateThickProps)=

# MidPlane.CreateThickProps

## Description

create thickness properties for mid-plane

## Syntax

```python
MidPlane.CreateThickProps(crlPart=[], dThickDiff=0.1, dMaxThick=DFLT_DBL, dMinThick=DFLT_DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT_DBL, dMatOrientY=DFLT_DBL, dMatOrientZ=DFLT_DBL, crCoord=None, dThickness=DFLT_DBL, dBendStiff=DFLT_DBL, dThickRatio=1, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL, dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```

Macro: {ref}`Macro-MidPlane-MidPlaneCreateThickProps`

Ribbon: {menuselection}`MidPlane --> CreateThickProps`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dThickDiff`**
: A _Double_ specifying the thickness difference. The default value is 0.1.

**`dMaxThick`**
: A _Double_ specifying the maximum thickness. The default value is DFLT_DBL.

**`dMinThick`**
: A _Double_ specifying the minimum thickness. The default value is DFLT_DBL.

**`crMatMembrane`**
: A _Cursor_ specifying the material membrane. The default value is None.

**`crMatBend`**
: A _Cursor_ specifying the material bend. The default value is None.

**`crMatShear`**
: A _Cursor_ specifying the material shear. The default value is None.

**`crMatCoupl`**
: A _Cursor_ specifying the material couple. The default value is None.

**`iMatOrientType`**
: An _Integer_ specifying the material orient type. The default value is 0.

**`dMatOrientX`**
: A _Double_ specifying the material orient x. The default value is DFLT_DBL.

**`dMatOrientY`**
: A _Double_ specifying the material orient y. The default value is DFLT_DBL.

**`dMatOrientZ`**
: A _Double_ specifying the material orient z. The default value is DFLT_DBL.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dThickness`**
: A _Double_ specifying the thickness. The default value is DFLT_DBL.

**`dBendStiff`**
: A _Double_ specifying the bend stiff. The default value is DFLT_DBL.

**`dThickRatio`**
: A _Double_ specifying the thickness ratio. The default value is 1.

**`dNSM`**
: A _Double_ specifying the n s m. The default value is DFLT_DBL.

**`dFiberDist1`**
: A _Double_ specifying the fiber distance 1. The default value is DFLT_DBL.

**`dFiberDist2`**
: A _Double_ specifying the fiber distance 2. The default value is DFLT_DBL.

**`dPlateOff`**
: A _Double_ specifying the plate off. The default value is DFLT_DBL.

**`iNumInterPts`**
: An _Integer_ specifying the number inter pts. The default value is 0.

**`bThickSetting`**
: A _Boolean_ specifying the thickness setting. The default value is False.

**`iEntityType`**
: An _Integer_ specifying the entity type. The default value is 0.

**`bDivideProp`**
: A _Boolean_ specifying the divide property. The default value is False.

**`crlRefPart`**
: A _Cursor List_ specifying the reference part. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlane.CreateThickProps(crlPart=[], dThickDiff=0.1, dMaxThick=DFLT_DBL, dMinThick=DFLT_DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT_DBL, dMatOrientY=DFLT_DBL, dMatOrientZ=DFLT_DBL, crCoord=None, dThickness=DFLT_DBL, dBendStiff=DFLT_DBL, dThickRatio=1, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL, dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```
