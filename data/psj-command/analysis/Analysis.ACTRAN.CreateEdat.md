```{module} Analysis.ACTRAN.CreateEdat()
:synopsis: Unknown Description
```

(Analysis.ACTRAN.CreateEdat)=

# Analysis.ACTRAN.CreateEdat

## Description

Unknown Description

## Syntax

```python
Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AnalysisActranJob`

Ribbon: {menuselection}`Analysis --> ACTRAN --> CreateEdat`

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
Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)
```
