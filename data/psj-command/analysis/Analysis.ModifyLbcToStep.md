```{module} Analysis.ModifyLbcToStep()
:synopsis: Abaqus analysis output data setting
```

(Analysis.ModifyLbcToStep)=

# Analysis.ModifyLbcToStep

## Description

Abaqus analysis output data setting

## Syntax

```python
Analysis.ModifyLbcToStep(listAbaqusLbcStepInfo=[])
```

Macro: {ref}`Macro-Analysis-AbaModifyLbcToStep`

Ribbon: {menuselection}`Analysis --> ModifyLbcToStep`

## Inputs

**`listAbaqusLbcStepInfo`**
: A _ABAQUS_LBC_STEP_INFO List_ specifying the abaqus load boundary condition step info. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ModifyLbcToStep(listAbaqusLbcStepInfo=[])
```
