```{module} Analysis.ADVC.MakeProcess.ModalFreqResp()
:synopsis: create modal frequency response process of ADVC
```

(Analysis.ADVC.MakeProcess.ModalFreqResp)=

# Analysis.ADVC.MakeProcess.ModalFreqResp

## Description

create modal frequency response process of ADVC

## Syntax

```python
Analysis.ADVC.MakeProcess.ModalFreqResp(strName, strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcModalFreqRespProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> ModalFreqResp`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strRefEigenDir`**
: A _String_ specifying the reference eigen direction. The default value is "".

**`dRefLowFreq`**
: A _Double_ specifying the reference low frequence. The default value is DFLT_DBL.

**`dRefHighFreq`**
: A _Double_ specifying the reference high frequence. The default value is DFLT_DBL.

**`crModalDampingRatio`**
: A _Cursor_ specifying the modal damping ratio. The default value is None.

**`crExcitationFreq`**
: A _Cursor_ specifying the excitation frequence. The default value is None.

**`bAutoFreqInterval`**
: A _Boolean_ specifying the auto frequence interval. The default value is False.

**`dMaxFreq`**
: A _Double_ specifying the maximum frequence. The default value is DFLT_DBL.

**`dMinFreq`**
: A _Double_ specifying the minimum frequence. The default value is DFLT_DBL.

**`iNumFreqPoint`**
: An _Integer_ specifying the number frequence point. The default value is DFLT_INT.

**`dBiasParam`**
: A _Double_ specifying the bias param. The default value is DFLT_DBL.

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
Analysis.ADVC.MakeProcess.ModalFreqResp(strName, strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
