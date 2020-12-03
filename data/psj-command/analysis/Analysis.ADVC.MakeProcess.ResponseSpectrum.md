```{module} Analysis.ADVC.MakeProcess.ResponseSpectrum()
:synopsis: create advc response spectrum process
```

(Analysis.ADVC.MakeProcess.ResponseSpectrum)=

# Analysis.ADVC.MakeProcess.ResponseSpectrum

## Description

create advc response spectrum process

## Syntax

```python
Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT_DBL, crSpt0=None, dSptFactor1=DFLT_DBL, crSpt1=None, dSptFactor2=DFLT_DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcSpectrumProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> ResponseSpectrum`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`strRefEigenDir`**
: A _String_ specifying the reference eigen direction. The default value is "".

**`dRefLowFreq`**
: A _Double_ specifying the reference low frequence. The default value is DFLT_DBL.

**`dRefHighFreq`**
: A _Double_ specifying the reference high frequence. The default value is DFLT_DBL.

**`iPropMethod`**
: An _Integer_ specifying the property method. The default value is 0.

**`iSpttype`**
: An _Integer_ specifying the spectrum type. The default value is 0.

**`dSptFactor0`**
: A _Double_ specifying the spectrum factor0. The default value is DFLT_DBL.

**`crSpt0`**
: A _Cursor_ specifying the spt0. The default value is None.

**`dSptFactor1`**
: A _Double_ specifying the spectrum factor1. The default value is DFLT_DBL.

**`crSpt1`**
: A _Cursor_ specifying the spectrum 1. The default value is None.

**`dSptFactor2`**
: A _Double_ specifying the spectrum factor2. The default value is DFLT_DBL.

**`crSpt2`**
: A _Cursor_ specifying the spectrum 2. The default value is None.

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
: An _Integer_ specifying the reference type. The default value is 0.

**`strRefPath`**
: A _String_ specifying the reference path. The default value is "".

**`listAdvcRefStressResult`**
: A _ADVC_REF_STRESS_RESULT List_ specifying the advc reference stress result. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT_DBL, crSpt0=None, dSptFactor1=DFLT_DBL, crSpt1=None, dSptFactor2=DFLT_DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])
```
