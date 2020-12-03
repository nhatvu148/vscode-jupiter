```{module} BoundaryConditions.LBCCopyMisc()
:synopsis: Unknown Description
```

(BoundaryConditions.LBCCopyMisc)=

# BoundaryConditions.LBCCopyMisc

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTarget=[])
```

Macro: {ref}`Macro-BoundaryConditions-CmdLbcCopy`

Ribbon: {menuselection}`BoundaryConditions --> LBCCopyMisc`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatchMethod`**
: An _Integer_ specifying the match method. The default value is 0.

**`dlTransVec`**
: A _Double List_ specifying the trans vector. The default value is [0,0,0].

**`dTransMag`**
: A _Double_ specifying the trans mag. The default value is 0.

**`dTransOffset`**
: A _Double_ specifying the trans offset. The default value is 0.

**`dTransTol`**
: A _Double_ specifying the trans tolerance. The default value is 0.

**`crTranscrCoord`**
: A _Cursor_ specifying the transcr coordinate. The default value is None.

**`dlTransaxisVec`**
: A _Double List_ specifying the transaxis vector. The default value is [0,0,0].

**`dlTranscenterVec`**
: A _Double List_ specifying the transcenter vector. The default value is [0,0,0].

**`dRotateAngle`**
: A _Double_ specifying the rotate angle. The default value is 0.

**`dRotateTol`**
: A _Double_ specifying the rotate tolerance. The default value is 0.

**`crRotatecrCoord`**
: A _Cursor_ specifying the rotatecr coordinate. The default value is None.

**`veclMirrorPoint`**
: A _Vector List_ specifying the mirror point. The default value is [].

**`dMirrordOffset`**
: A _Double_ specifying the mirrord offset. The default value is 0.

**`dMirrorTol`**
: A _Double_ specifying the mirror tolerance. The default value is 0.1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTarget=[])
```
