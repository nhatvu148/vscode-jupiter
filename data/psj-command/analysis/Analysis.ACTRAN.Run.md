```{module} Analysis.ACTRAN.Run()
:synopsis: Unknown Description
```

(Analysis.ACTRAN.Run)=

# Analysis.ACTRAN.Run

## Description

Unknown Description

## Syntax

```python
Analysis.ACTRAN.Run(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AnalysisActranRun`

Ribbon: {menuselection}`Analysis --> ACTRAN --> Run`

## Inputs

**`actranAnalysis`**
: A _ACTRAN_ANALYSIS_ specifying the actran analysis data structure. The default value is ACTRAN_ANALYSIS().

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ACTRAN.Run(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)
```
