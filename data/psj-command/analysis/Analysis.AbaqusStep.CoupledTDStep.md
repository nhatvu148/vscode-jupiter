```{module} Analysis.AbaqusStep.CoupledTDStep()
:synopsis: create abaqus step of coupled Temp-Displacement
```

(Analysis.AbaqusStep.CoupledTDStep)=

# Analysis.AbaqusStep.CoupledTDStep

## Description

create abaqus step of coupled Temp-Displacement

## Syntax

```python
Analysis.AbaqusStep.CoupledTDStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, abaqusPair1=ABAQUS_PAIR(), abaqusPair2=ABAQUS_PAIR(), iCSVIntegration=0, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, dAdjustFactor=1.0, iMaxContactIter=30, iType=0, iEnableUseAdaptive=1, dDampingfactor=0.0002, dMaxRationofStrainEnergy=0.05, iEnableNlgeom=0, dTimePeriod=1.0, iTransient=1, iConvertDscntIter=0, iRamp=1, iExtrapolateMethod=0, iEnableIncludeCSV=0, listAbaqusOutputRequest=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusCoupledTDStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> CoupledTDStep`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strDesp`**
: A _String_ specifying the description. The default value is "".

**`iEnableAutomatic`**
: An _Integer_ specifying the enable automatic. The default value is 0.

**`iMaxInc`**
: An _Integer_ specifying the maximum increment. The default value is 100.

**`dInitSize`**
: A _Double_ specifying the initial size. The default value is 1.0.

**`dMinSize`**
: A _Double_ specifying the minimum size. The default value is 1.0e-5.

**`dMaxSize`**
: A _Double_ specifying the maximum size. The default value is 1.0.

**`abaqusPair1`**
: A _ABAQUS_PAIR1_ specifying the abaqus pair 1 data structure. The default value is ABAQUS_PAIR().

**`abaqusPair2`**
: A _ABAQUS_PAIR2_ specifying the abaqus pair 2 data structure. The default value is ABAQUS_PAIR().

**`iCSVIntegration`**
: An _Integer_ specifying the CSV integration. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatrixStorage`**
: An _Integer_ specifying the matrix storage. The default value is 0.

**`iSolutionTech`**
: An _Integer_ specifying the solution technology. The default value is 0.

**`iAllowedIters`**
: An _Integer_ specifying the allowed iterators. The default value is 8.

**`dAdjustFactor`**
: A _Double_ specifying the adjust factor. The default value is 1.0.

**`iMaxContactIter`**
: An _Integer_ specifying the maximum contact iterator. The default value is 30.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iEnableUseAdaptive`**
: An _Integer_ specifying the enable use adaptive. The default value is 1.

**`dDampingfactor`**
: A _Double_ specifying the dampingfactor. The default value is 0.0002.

**`dMaxRationofStrainEnergy`**
: A _Double_ specifying the maximum rationof strain energy. The default value is 0.05.

**`iEnableNlgeom`**
: An _Integer_ specifying the enable nlgeom. The default value is 0.

**`dTimePeriod`**
: A _Double_ specifying the time period. The default value is 1.0.

**`iTransient`**
: An _Integer_ specifying the transient. The default value is 1.

**`iConvertDscntIter`**
: An _Integer_ specifying the convert destination count iterator. The default value is 0.

**`iRamp`**
: An _Integer_ specifying the ramp. The default value is 1.

**`iExtrapolateMethod`**
: An _Integer_ specifying the extrapolate method. The default value is 0.

**`iEnableIncludeCSV`**
: An _Integer_ specifying the enable include CSV. The default value is 0.

**`listAbaqusOutputRequest`**
: A _ABAQUS_OUTPUT_REQUEST List_ specifying the abaqus output request. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.CoupledTDStep(strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, abaqusPair1=ABAQUS_PAIR(), abaqusPair2=ABAQUS_PAIR(), iCSVIntegration=0, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, dAdjustFactor=1.0, iMaxContactIter=30, iType=0, iEnableUseAdaptive=1, dDampingfactor=0.0002, dMaxRationofStrainEnergy=0.05, iEnableNlgeom=0, dTimePeriod=1.0, iTransient=1, iConvertDscntIter=0, iRamp=1, iExtrapolateMethod=0, iEnableIncludeCSV=0, listAbaqusOutputRequest=[], crEdit=None)
```
