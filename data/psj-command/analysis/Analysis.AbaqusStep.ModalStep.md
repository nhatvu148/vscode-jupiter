```{module} Analysis.AbaqusStep.ModalStep()
:synopsis:
```

(Analysis.AbaqusStep.ModalStep)=

# Analysis.AbaqusStep.ModalStep

## Description

## Syntax

```python
Analysis.AbaqusStep.ModalStep(strName, strDesp="", iEigenSolver=0, iNFreqRequestbchecked=0, ilNFreqRequestTList=[], iFreqShiftbchecked=0, ilFreqShiftTList=[], iFreqRangebchecked=0, ilFreqRangeTList=[], iIncldAcoustic=0, iBlockSizebchecked=0, ilBlockSizeTList=[], iMaxBlkNumofLanczosStepbchecked=0, ilMaxBlkNumofLanczosStepTList=[], iEnableUseSIM=0, iEnableIncludeResMods=0, iNEigenRequest=2147483647, iMaxItersUsed=30, iVectorsUsed=2147483647, iMethod=0, iMatrixStorage=0, iNormalizeEigenBy=1, iEvalPropFreqbchecked=0, ilEvalPropFreqTList=[], abaqusOutputRequest=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusModalStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> ModalStep`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strDesp`**
: A _String_ specifying the description. The default value is "".

**`iEigenSolver`**
: An _Integer_ specifying the eigen solver. The default value is 0.

**`iNFreqRequestbchecked`**
: An _Integer_ specifying the frequence request check. The default value is 0.

**`ilNFreqRequestTList`**
: A _Integer List_ specifying the frequence request table list. The default value is [].

**`iFreqShiftbchecked`**
: An _Integer_ specifying the frequence shiftbchecked. The default value is 0.

**`ilFreqShiftTList`**
: A _Integer List_ specifying the frequence shift table list. The default value is [].

**`iFreqRangebchecked`**
: An _Integer_ specifying the frequence range check. The default value is 0.

**`ilFreqRangeTList`**
: A _Integer List_ specifying the frequence range table list. The default value is [].

**`iIncldAcoustic`**
: An _Integer_ specifying the include acoustic. The default value is 0.

**`iBlockSizebchecked`**
: An _Integer_ specifying the block size check. The default value is 0.

**`ilBlockSizeTList`**
: A _Integer List_ specifying the block size table list. The default value is [].

**`iMaxBlkNumofLanczosStepbchecked`**
: An _Integer_ specifying the maximum block number of lanczos step check. The default value is 0.

**`ilMaxBlkNumofLanczosStepTList`**
: A _Integer List_ specifying the maximum block number of lanczos step table list. The default value is [].

**`iEnableUseSIM`**
: An _Integer_ specifying the enable use s i m. The default value is 0.

**`iEnableIncludeResMods`**
: An _Integer_ specifying the enable include result modes. The default value is 0.

**`iNEigenRequest`**
: An _Integer_ specifying the n eigen request. The default value is 2147483647.

**`iMaxItersUsed`**
: An _Integer_ specifying the maximum iterators used. The default value is 30.

**`iVectorsUsed`**
: An _Integer_ specifying the vectors used. The default value is 2147483647.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatrixStorage`**
: An _Integer_ specifying the matrix storage. The default value is 0.

**`iNormalizeEigenBy`**
: An _Integer_ specifying the normalize eigen by. The default value is 1.

**`iEvalPropFreqbchecked`**
: An _Integer_ specifying the evaluation property freqbchecked. The default value is 0.

**`ilEvalPropFreqTList`**
: A _Integer List_ specifying the evaluation property frequence table list. The default value is [].

**`abaqusOutputRequest`**
: A _ABAQUS_OUTPUT_REQUEST_ specifying the output request. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.ModalStep(strName, strDesp="", iEigenSolver=0, iNFreqRequestbchecked=0, ilNFreqRequestTList=[], iFreqShiftbchecked=0, ilFreqShiftTList=[], iFreqRangebchecked=0, ilFreqRangeTList=[], iIncldAcoustic=0, iBlockSizebchecked=0, ilBlockSizeTList=[], iMaxBlkNumofLanczosStepbchecked=0, ilMaxBlkNumofLanczosStepTList=[], iEnableUseSIM=0, iEnableIncludeResMods=0, iNEigenRequest=2147483647, iMaxItersUsed=30, iVectorsUsed=2147483647, iMethod=0, iMatrixStorage=0, iNormalizeEigenBy=1, iEvalPropFreqbchecked=0, ilEvalPropFreqTList=[], abaqusOutputRequest=[], crEdit=None)
```
