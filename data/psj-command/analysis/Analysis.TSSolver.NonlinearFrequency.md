```{module} Analysis.TSSolver.NonlinearFrequency()
:synopsis: Export TS-Solver Nonlinear Frequency
```

(Analysis.TSSolver.NonlinearFrequency)=

# Analysis.TSSolver.NonlinearFrequency

## Description

Export TS-Solver Nonlinear Frequency

## Syntax

```python
Analysis.TSSolver.NonlinearFrequency(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")
```

Macro: {ref}`Macro-Analysis-TSSolverNonlinearFrequency`

Ribbon: {menuselection}`Analysis --> TSSolver --> NonlinearFrequency`

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

**`strPath`**
: A _String_ specifying the path. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.TSSolver.NonlinearFrequency(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")
```
