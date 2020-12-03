```{module} Analysis.AbaqusStep.DynamicStep()
:synopsis: Unknown Description
```

(Analysis.AbaqusStep.DynamicStep)=

# Analysis.AbaqusStep.DynamicStep

## Description

Unknown Description

## Syntax

```python
Analysis.AbaqusStep.DynamicStep(abaqusDynamic=ABAQUS_DYNAMIC(), crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusDynamicStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> DynamicStep`

## Inputs

**`abaqusDynamic`**
: A _ABAQUS_DYNAMIC_ specifying the abaqus dynamic. The default value is ABAQUS_DYNAMIC().

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.DynamicStep(abaqusDynamic=ABAQUS_DYNAMIC(), crEdit=None)
```
