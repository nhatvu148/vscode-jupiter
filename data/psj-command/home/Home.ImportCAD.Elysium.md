```{module} Home.ImportCAD.Elysium()
:synopsis: import elysium
```

(Home.ImportCAD.Elysium)=

# Home.ImportCAD.Elysium

## Description

import elysium

## Syntax

```python
Home.ImportCAD.Elysium(strlPath=[], dChordHeightTolerance=1.0, dAngleToleranceDegree=5.0, dPointCoincidentTolerance=0.01, iConvertIsolatedCurve=0, iDekCleanselfintersectingloop=2, iDekVolumetopart=4, iIgesFixedcurevepreference=0, iIgesAutostitch=1, dIgesStitchtolerance=0.1, iCatiaConvertnotshowedelement=0, iCatiaConvertnotshowedinstance=0, iCatiaConvertaxis=1, iStepCreateseam=1, dStepPointtolerance=0.0, iAcisHealacisbeforeversion=0, iJtConvertgeometrytype=2, bFaceColor=False, iJtConvertgeneralpart=1, iJtConvertaxis=1, iJtConvertcenterline=0)
```

Macro: {ref}`Macro-Home-ImportElysium`

Ribbon: {menuselection}`Home --> ImportCAD --> Elysium`

## Inputs

**`strlPath`**
: A _String List_ specifying the path. The default value is [].

**`dChordHeightTolerance`**
: A _Double_ specifying the chord height tolerance. The default value is 1.0.

**`dAngleToleranceDegree`**
: A _Double_ specifying the angle tolerance degree. The default value is 5.0.

**`dPointCoincidentTolerance`**
: A _Double_ specifying the point coincident tolerance. The default value is 0.01.

**`iConvertIsolatedCurve`**
: An _Integer_ specifying the convert isolated curve. The default value is 0.

**`iDekCleanselfintersectingloop`**
: An _Integer_ specifying the dek clean self intersecting loop. The default value is 2.

**`iDekVolumetopart`**
: An _Integer_ specifying the dek volume to part. The default value is 4.

**`iIgesFixedcurevepreference`**
: An _Integer_ specifying the iges fixed cureve preference. The default value is 0.

**`iIgesAutostitch`**
: An _Integer_ specifying the iges auto stitch. The default value is 1.

**`dIgesStitchtolerance`**
: A _Double_ specifying the iges stitch tolerance. The default value is 0.1.

**`iCatiaConvertnotshowedelement`**
: An _Integer_ specifying the catia convert not showed element. The default value is 0.

**`iCatiaConvertnotshowedinstance`**
: An _Integer_ specifying the catia convert not showed instance. The default value is 0.

**`iCatiaConvertaxis`**
: An _Integer_ specifying the catia convert axis. The default value is 1.

**`iStepCreateseam`**
: An _Integer_ specifying the step create seam. The default value is 1.

**`dStepPointtolerance`**
: A _Double_ specifying the step point tolerance. The default value is 0.0.

**`iAcisHealacisbeforeversion`**
: An _Integer_ specifying the acis heal acis before version. The default value is 0.

**`iJtConvertgeometrytype`**
: An _Integer_ specifying the jupiter convert geometry type. The default value is 2.

**`bFaceColor`**
: A _Boolean_ specifying the face color. The default value is False.

**`iJtConvertgeneralpart`**
: An _Integer_ specifying the jupiter convert general part. The default value is 1.

**`iJtConvertaxis`**
: An _Integer_ specifying the jupiter convert axis. The default value is 1.

**`iJtConvertcenterline`**
: An _Integer_ specifying the jupiter convert center line. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportCAD.Elysium(strlPath=[], dChordHeightTolerance=1.0, dAngleToleranceDegree=5.0, dPointCoincidentTolerance=0.01, iConvertIsolatedCurve=0, iDekCleanselfintersectingloop=2, iDekVolumetopart=4, iIgesFixedcurevepreference=0, iIgesAutostitch=1, dIgesStitchtolerance=0.1, iCatiaConvertnotshowedelement=0, iCatiaConvertnotshowedinstance=0, iCatiaConvertaxis=1, iStepCreateseam=1, dStepPointtolerance=0.0, iAcisHealacisbeforeversion=0, iJtConvertgeometrytype=2, bFaceColor=False, iJtConvertgeneralpart=1, iJtConvertaxis=1, iJtConvertcenterline=0)
```
