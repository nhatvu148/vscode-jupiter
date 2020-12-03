```{module} Analysis.AbaqusStep.TransientStep()
:synopsis:
```

(Analysis.AbaqusStep.TransientStep)=

# Analysis.AbaqusStep.TransientStep

## Description

## Syntax

```python
Analysis.AbaqusStep.TransientStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=0, dInitSize=DFLT_DBL, dMinSize=DFLT_DBL, dMaxSize=DFLT_DBL, dMaxAllowTChange=DFLT_DBL, iEndsteptBchecked=0, dlEndsteptTlist=[], dMaxAllowEmissivityChange=DFLT_DBL, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=0, dAdjustFactor=DFLT_DBL, iMaxContactIter=0, iEnableNlgeom=0, dTimePeriod=DFLT_DBL, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, listAbaqusOutputRequest=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusTransientStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> TransientStep`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`strDesp`**
: A _String_ specifying the description. The default value is "".

**`iEnableAutomatic`**
: An _Integer_ specifying the enable automatic. The default value is 0.

**`iMaxInc`**
: An _Integer_ specifying the maximum increment. The default value is 0.

**`dInitSize`**
: A _Double_ specifying the initial size. The default value is DFLT_DBL.

**`dMinSize`**
: A _Double_ specifying the minimum size. The default value is DFLT_DBL.

**`dMaxSize`**
: A _Double_ specifying the maximum size. The default value is DFLT_DBL.

**`dMaxAllowTChange`**
: A _Double_ specifying the maximum allow t change. The default value is DFLT_DBL.

**`iEndsteptBchecked`**
: An _Integer_ specifying the end step time check. The default value is 0.

**`dlEndsteptTlist`**
: A _Double List_ specifying the end step time table list. The default value is [].

**`dMaxAllowEmissivityChange`**
: A _Double_ specifying the maximum allow emissivity change. The default value is DFLT_DBL.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatrixStorage`**
: An _Integer_ specifying the matrix storage. The default value is 0.

**`iSolutionTech`**
: An _Integer_ specifying the solution technology. The default value is 0.

**`iAllowedIters`**
: An _Integer_ specifying the allowed iterators. The default value is 0.

**`dAdjustFactor`**
: A _Double_ specifying the adjust factor. The default value is DFLT_DBL.

**`iMaxContactIter`**
: An _Integer_ specifying the maximum contact iterator. The default value is 0.

**`iEnableNlgeom`**
: An _Integer_ specifying the enable nlgeom. The default value is 0.

**`dTimePeriod`**
: A _Double_ specifying the time period. The default value is DFLT_DBL.

**`iConvertDscntIter`**
: An _Integer_ specifying the convert destination count iterator. The default value is 0.

**`iRamp`**
: An _Integer_ specifying the ramp. The default value is 0.

**`iExtrapolateMethod`**
: An _Integer_ specifying the extrapolate method. The default value is 0.

**`listAbaqusOutputRequest`**
: A _ABAQUS_OUTPUT_REQUEST List_ specifying the abaqus output request. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.TransientStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=0, dInitSize=DFLT_DBL, dMinSize=DFLT_DBL, dMaxSize=DFLT_DBL, dMaxAllowTChange=DFLT_DBL, iEndsteptBchecked=0, dlEndsteptTlist=[], dMaxAllowEmissivityChange=DFLT_DBL, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=0, dAdjustFactor=DFLT_DBL, iMaxContactIter=0, iEnableNlgeom=0, dTimePeriod=DFLT_DBL, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, listAbaqusOutputRequest=[], crEdit=None)
```
