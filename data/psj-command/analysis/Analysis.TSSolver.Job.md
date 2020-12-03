```{module} Analysis.TSSolver.Job()
:synopsis: Create TS-Solver Job
```

(Analysis.TSSolver.Job)=

# Analysis.TSSolver.Job

## Description

Create TS-Solver Job

## Syntax

```python
Analysis.TSSolver.Job(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None)
```

Macro: {ref}`Macro-Analysis-DynamisJob`

Ribbon: {menuselection}`Analysis --> TSSolver --> Job`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`nastranAnalysis`**
: A _NASTRAN_ANALYSIS_ specifying the nastran analysis data structure. The default value is NASTRAN_ANALYSIS().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.TSSolver.Job(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None)
```
