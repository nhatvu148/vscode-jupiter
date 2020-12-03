```{module} Analysis.AbaqusStep.SteadyStateStep()
:synopsis: Abaqus Steady State Step
```

(Analysis.AbaqusStep.SteadyStateStep)=

# Analysis.AbaqusStep.SteadyStateStep

## Description

Abaqus Steady State Step

## Syntax

```python
Analysis.AbaqusStep.SteadyStateStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, iNitSize=1, dMinSize=1.0e-5, dMaxSize=1.0, dMaxAllowTChange=DFLT_DBL, iEndStepbchecked=0, dlEndStepTList=[], dMaxAllowEmissivityChange=0.1, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, iAdjustFactor=1, iMaxContactIter=30, iEnableNlgeom=0, dTimePeriod=1.0, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, iOutput=0, crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusSteadyStateStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> SteadyStateStep`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strDesp`**
: A _String_ specifying the description. The default value is "".

**`iEnableAutomatic`**
: An _Integer_ specifying the enable automatic. The default value is 0.

**`iMaxInc`**
: An _Integer_ specifying the maximum increment. The default value is 100.

**`iNitSize`**
: An _Integer_ specifying the initial size. The default value is 1.

**`dMinSize`**
: A _Double_ specifying the minimum size. The default value is 1.0e-5.

**`dMaxSize`**
: A _Double_ specifying the maximum size. The default value is 1.0.

**`dMaxAllowTChange`**
: A _Double_ specifying the maximum allow table change. The default value is DFLT_DBL.

**`iEndStepbchecked`**
: An _Integer_ specifying the end step check. The default value is 0.

**`dlEndStepTList`**
: A _Double List_ specifying the end step table list. The default value is [].

**`dMaxAllowEmissivityChange`**
: A _Double_ specifying the maximum allow emissivity change. The default value is 0.1.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatrixStorage`**
: An _Integer_ specifying the matrix storage. The default value is 0.

**`iSolutionTech`**
: An _Integer_ specifying the solution technology. The default value is 0.

**`iAllowedIters`**
: An _Integer_ specifying the allowed iterators. The default value is 8.

**`iAdjustFactor`**
: An _Integer_ specifying the adjust factor. The default value is 1.

**`iMaxContactIter`**
: An _Integer_ specifying the maximum contact iterator. The default value is 30.

**`iEnableNlgeom`**
: An _Integer_ specifying the enable nlgeom. The default value is 0.

**`dTimePeriod`**
: A _Double_ specifying the time period. The default value is 1.0.

**`iConvertDscntIter`**
: An _Integer_ specifying the convert destination count iterator. The default value is 0.

**`iRamp`**
: An _Integer_ specifying the ramp. The default value is 0.

**`iExtrapolateMethod`**
: An _Integer_ specifying the extrapolate method. The default value is 0.

**`iOutput`**
: An _Integer_ specifying the output. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.SteadyStateStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, iNitSize=1, dMinSize=1.0e-5, dMaxSize=1.0, dMaxAllowTChange=DFLT_DBL, iEndStepbchecked=0, dlEndStepTList=[], dMaxAllowEmissivityChange=0.1, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, iAdjustFactor=1, iMaxContactIter=30, iEnableNlgeom=0, dTimePeriod=1.0, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, iOutput=0, crEdit=None)
```
