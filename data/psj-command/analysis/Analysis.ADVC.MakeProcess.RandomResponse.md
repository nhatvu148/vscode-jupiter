```{module} Analysis.ADVC.MakeProcess.RandomResponse()
:synopsis: create advc random response process
```

(Analysis.ADVC.MakeProcess.RandomResponse)=

# Analysis.ADVC.MakeProcess.RandomResponse

## Description

create advc random response process

## Syntax

```python
Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT_DBL, dGravityAccel=DFLT_DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcRandomProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> RandomResponse`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

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

**`iPropMethod`**
: An _Integer_ specifying the property method. The default value is 0.

**`iPSDtype`**
: An _Integer_ specifying the PSD type. The default value is -1.

**`iPSDdir`**
: An _Integer_ specifying the PSD ddir. The default value is 0.

**`crPSDLoad`**
: A _Cursor_ specifying the PSD load. The default value is None.

**`dPSDFactor`**
: A _Double_ specifying the PSD factor. The default value is DFLT_DBL.

**`dGravityAccel`**
: A _Double_ specifying the gravity accel. The default value is DFLT_DBL.

**`iOutputEigenFreqStep`**
: An _Integer_ specifying the output eigen frequence step. The default value is -1.

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
Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT_DBL, dGravityAccel=DFLT_DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
