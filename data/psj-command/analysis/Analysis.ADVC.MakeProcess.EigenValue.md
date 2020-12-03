```{module} Analysis.ADVC.MakeProcess.EigenValue()
:synopsis: create advc eigen value process
```

(Analysis.ADVC.MakeProcess.EigenValue)=

# Analysis.ADVC.MakeProcess.EigenValue

## Description

create advc eigen value process

## Syntax

```python
Analysis.ADVC.MakeProcess.EigenValue(strName, bEigenValue=False, iNumberOfModes=0, iEigenvecNorm=10, dShift=DFLT_DBL, dCgcgpiTol=DFLT_DBL, dCgcgpiEigTol=DFLT_DBL, iCgcgpiLoopMax=DFLT_INT, dCgcgpiInnerTol=DFLT_DBL, iCgcgpiBlockSize=DFLT_INT, iCgcgpiExtraMode=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcEigenProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> EigenValue`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`bEigenValue`**
: A _Boolean_ specifying the eigen value. The default value is False.

**`iNumberOfModes`**
: An _Integer_ specifying the number of modes. The default value is 0.

**`iEigenvecNorm`**
: An _Integer_ specifying the eigenvec norm. The default value is 10.

**`dShift`**
: A _Double_ specifying the shift. The default value is DFLT_DBL.

**`dCgcgpiTol`**
: A _Double_ specifying the cgcgpi tolerance. The default value is DFLT_DBL.

**`dCgcgpiEigTol`**
: A _Double_ specifying the cgcgpi eig tolerance. The default value is DFLT_DBL.

**`iCgcgpiLoopMax`**
: An _Integer_ specifying the cgcgpi loop maximum. The default value is DFLT_INT.

**`dCgcgpiInnerTol`**
: A _Double_ specifying the cgcgpi inner tolerance. The default value is DFLT_DBL.

**`iCgcgpiBlockSize`**
: An _Integer_ specifying the cgcgpi block size. The default value is DFLT_INT.

**`iCgcgpiExtraMode`**
: An _Integer_ specifying the cgcgpi extra mode. The default value is DFLT_INT.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`listLoadNode`**
: A _LOAD_NODE List_ specifying the load node. The default value is [].

**`listLoadCaseNode`**
: A _LOAD_CASE_NODE List_ specifying the load case node. The default value is [].

**`listLoadNodeContact`**
: A _LOAD_NODE_CONTACT List_ specifying the load node contact. The default value is [].

**`ilOutputParamList`**
: A _Integer List_ specifying the output param list. The default value is [].

**`iRefType`**
: An _Integer_ specifying the reference type. The default value is -1.

**`strRefPath`**
: A _String_ specifying the reference path. The default value is "".

**`listAdvcRefStressResult`**
: A _ADVC_REF_STRESS_RESULT List_ specifying the advc reference stress result. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ADVC.MakeProcess.EigenValue(strName, bEigenValue=False, iNumberOfModes=0, iEigenvecNorm=10, dShift=DFLT_DBL, dCgcgpiTol=DFLT_DBL, dCgcgpiEigTol=DFLT_DBL, iCgcgpiLoopMax=DFLT_INT, dCgcgpiInnerTol=DFLT_DBL, iCgcgpiBlockSize=DFLT_INT, iCgcgpiExtraMode=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
