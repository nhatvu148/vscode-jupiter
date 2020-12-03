```{module} Analysis.NastranJob()
:synopsis: Create nastran Job
```

(Analysis.NastranJob)=

# Analysis.NastranJob

## Description

Create nastran Job

## Syntax

```python
Analysis.NastranJob(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None)
```

Macro: {ref}`Macro-Analysis-NastranJob`

Ribbon: {menuselection}`Analysis --> NastranJob`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Job_1".

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`nastranAnalysis`**
: A _NASTRAN_ANALYSIS_ specifying the nastran analysis data structure. The default value is NASTRAN_ANALYSIS().

**`bDummyPropAutoAssign`**
: A _Boolean_ specifying the dummy property auto assign. The default value is False.

**`iDummyPropMaterialID`**
: An _Integer_ specifying the dummy property material ID. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.NastranJob(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None)
```
