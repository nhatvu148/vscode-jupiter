```{module} Analysis.TSSolver.NormalModes()
:synopsis: Export TS-Solver Normal Modes
```

(Analysis.TSSolver.NormalModes)=

# Analysis.TSSolver.NormalModes

## Description

Export TS-Solver Normal Modes

## Syntax

```python
Analysis.TSSolver.NormalModes(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")
```

Macro: {ref}`Macro-Analysis-TSSolverNormalModes`

Ribbon: {menuselection}`Analysis --> TSSolver --> NormalModes`

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
Analysis.TSSolver.NormalModes(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")
```
