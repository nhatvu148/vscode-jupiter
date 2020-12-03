```{module} SNOnePush.CADImport()
:synopsis: import CAD model
```

(SNOnePush.CADImport)=

# SNOnePush.CADImport

## Description

import CAD model

## Syntax

```python
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```

Macro: {ref}`Macro-SNOnePush-SonyOnePushCadImport`

Ribbon: {menuselection}`SNOnePush --> CADImport`

## Inputs

**`dDsurfaceplaneTolerance`**
: A _Double_ specifying the dsurfaceplane tolerance. This is a required input.

**`dDsurfaceplaneAngle`**
: A _Double_ specifying the dsurfaceplane angle. This is a required input.

**`dMaxFacetWidth`**
: A _Double_ specifying the maximum facet width. This is a required input.

**`bBnxMultipart`**
: A _Boolean_ specifying the bnx multipart. This is a required input.

**`dChordHeightTolerance`**
: A _Double_ specifying the chord height tolerance. This is a required input.

**`dAngleToleranceDegree`**
: A _Double_ specifying the angle tolerance degree. This is a required input.

**`iConvertIsolatedCurve`**
: An _Integer_ specifying the convert isolated curve. This is a required input.

**`iIigesFixedcurevepreference`**
: An _Integer_ specifying the iiges fixed cureve preference. This is a required input.

**`iIigesAutostitch`**
: An _Integer_ specifying the iiges auto stitch. This is a required input.

**`dDigesStitchtolerance`**
: A _Double_ specifying the diges stitch tolerance. This is a required input.

**`iIcatiaConvertnotshowedelement`**
: An _Integer_ specifying the icatia convert not showed element. This is a required input.

**`iIcatiaConvertnotshowedinstance`**
: An _Integer_ specifying the icatia convert not showed instance. This is a required input.

**`iIcatiaConvertaxis`**
: An _Integer_ specifying the icatia convert axis. This is a required input.

**`iIstepCreateseam`**
: An _Integer_ specifying the istep create seam. This is a required input.

**`dDstepPointtolerance`**
: A _Double_ specifying the dstep point tolerance. This is a required input.

**`iIacisHealacisbeforeversion`**
: An _Integer_ specifying the iacis heal acis before version. This is a required input.

**`iIjtConvertgeometrytype`**
: An _Integer_ specifying the ijt convert geometry type. This is a required input.

**`iIjtConvertgeneralpart`**
: An _Integer_ specifying the ijt convert general part. This is a required input.

**`iIjtConvertaxis`**
: An _Integer_ specifying the ijt convert axis. This is a required input.

**`iIjtConvertcenterline`**
: An _Integer_ specifying the ijt convert center line. This is a required input.

**`dDcreoChordheighttolerance`**
: A _Double_ specifying the dcreo chord height tolerance. This is a required input.

**`dDcreoAngletolerancedegree`**
: A _Double_ specifying the dcreo angle tolerance degree. This is a required input.

**`strAbsCreoPath`**
: A _String_ specifying the abs creo path. This is a required input.

**`iTransType`**
: An _Integer_ specifying the trans type. This is a required input.

**`iFileType`**
: An _Integer_ specifying the file type. This is a required input.

**`strFilePath`**
: A _String_ specifying the file path. This is a required input.

**`bRenameDuplicateName`**
: A _Boolean_ specifying the rename duplicate name. This is a required input.

**`strCSVFilePath`**
: A _String_ specifying the CSV file path. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```
