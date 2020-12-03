```{module} Analysis.ADVC.Structure()
:synopsis: create advc job
```

(Analysis.ADVC.Structure)=

# Analysis.ADVC.Structure

## Description

create advc job

## Syntax

```python
Analysis.ADVC.Structure(strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, iCreateProcessForBoltFixedLength=0, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)
```

Macro: {ref}`Macro-Analysis-ADVC_Structure`

Ribbon: {menuselection}`Analysis --> ADVC --> Structure`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`iEJobType`**
: An _Integer_ specifying the e job type. The default value is 0.

**`crlProcessSequence`**
: A _Cursor List_ specifying the process sequence. The default value is [].

**`crlElemLocationGroup`**
: A _Cursor List_ specifying the element location group. The default value is [].

**`crlNodeLocationGroup`**
: A _Cursor List_ specifying the node location group. The default value is [].

**`bWriteGroup`**
: A _Boolean_ specifying the write group. The default value is False.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bResultReference`**
: A _Boolean_ specifying the result reference. The default value is False.

**`iSeparateFile`**
: An _Integer_ specifying the separate file. The default value is 0.

**`bExportRelatedAllLBCs`**
: A _Boolean_ specifying the export related all l cs. The default value is False.

**`bUseEntityName`**
: A _Boolean_ specifying the use entity name. The default value is False.

**`bMatrixSloverParam`**
: A _Boolean_ specifying the matrix slover param. The default value is False.

**`iPreconditionType`**
: An _Integer_ specifying the precondition type. The default value is 0.

**`iMatrixStructure`**
: An _Integer_ specifying the matrix structure. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iLoadType`**
: An _Integer_ specifying the load type. The default value is 1.

**`bSameOutputOnAllProcess`**
: A _Boolean_ specifying the same output on all process. The default value is True.

**`bDeleteFloatingNode`**
: A _Boolean_ specifying the delete floating node. The default value is True.

**`bBC`**
: A _Boolean_ specifying the boundary condition. The default value is True.

**`bCheckBCDuplicate`**
: A _Boolean_ specifying the check boundary condition duplicate. The default value is False.

**`bAutoAssignDummyProp`**
: A _Boolean_ specifying the auto assign dummy property. The default value is False.

**`crDummyPropMaterial`**
: A _Cursor_ specifying the dummy property material. The default value is None.

**`bReferenceRestartData`**
: A _Boolean_ specifying the reference restart data. The default value is False.

**`strReferenceRestartDataPath`**
: A _String_ specifying the reference restart data path. The default value is "".

**`iReferenceRestartDataProcessNum`**
: An _Integer_ specifying the reference restart data process number. The default value is DFLT_INT.

**`iReferenceRestartDataStepNum`**
: An _Integer_ specifying the reference restart data step number. The default value is DFLT_INT.

**`iReferenceRestartDataCoordType`**
: An _Integer_ specifying the reference restart data coordinate type. The default value is 0.

**`iReferenceRestartDataUpdateContactSearch`**
: An _Integer_ specifying the reference restart data update contact search. The default value is 1.

**`listLoadNodeContact`**
: A _LOAD_NODE_CONTACT List_ specifying the load node contact. The default value is [].

**`iHeatConvection`**
: An _Integer_ specifying the heat convection. The default value is 1.

**`iCreateProcessForBoltFixedLength`**
: An _Integer_ specifying the create process for bolt fixed length. The default value is 0.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`iNumType`**
: An _Integer_ specifying the number type. The default value is 0.

**`iUiWidth`**
: An _Integer_ specifying the UI width. The default value is 10.

**`iUiPrecision`**
: An _Integer_ specifying the UI precision. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ADVC.Structure(strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, iCreateProcessForBoltFixedLength=0, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)
```
