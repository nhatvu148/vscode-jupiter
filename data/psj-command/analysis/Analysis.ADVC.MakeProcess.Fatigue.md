```{module} Analysis.ADVC.MakeProcess.Fatigue()
:synopsis: create advc fatigue process
```

(Analysis.ADVC.MakeProcess.Fatigue)=

# Analysis.ADVC.MakeProcess.Fatigue

## Description

create advc fatigue process

## Syntax

```python
Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT_DBL, dSafetyMax=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcFatigueProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> Fatigue`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`bFatigue`**
: A _Boolean_ specifying the fatigue. The default value is False.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iStressAxis`**
: An _Integer_ specifying the stress axis. The default value is 0.

**`iSafetyType`**
: An _Integer_ specifying the safety type. The default value is 0.

**`dSearchResolution`**
: A _Double_ specifying the search resolution. The default value is DFLT_DBL.

**`dSafetyMax`**
: A _Double_ specifying the safety maximum. The default value is DFLT_DBL.

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
Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT_DBL, dSafetyMax=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
