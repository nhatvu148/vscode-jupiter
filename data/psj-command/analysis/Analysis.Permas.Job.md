```{module} Analysis.Permas.Job()
:synopsis: permas output
```

(Analysis.Permas.Job)=

# Analysis.Permas.Job

## Description

permas output

## Syntax

```python
Analysis.Permas.Job(strName, strDescription, iType, crEdit, crlTarget, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
```

Macro: {ref}`Macro-Analysis-PermasJob`

Ribbon: {menuselection}`Analysis --> Permas --> Job`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strDescription`**
: A _String_ specifying the description. This is a required input.

**`iType`**
: An _Integer_ specifying the type. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`bElStress`**
: A _Boolean_ specifying the el stress. This is a required input.

**`bElStressMis`**
: A _Boolean_ specifying the el stress mis. This is a required input.

**`bElStrain`**
: A _Boolean_ specifying the el strain. This is a required input.

**`bNodeStess`**
: A _Boolean_ specifying the node stess. This is a required input.

**`bGZip`**
: A _Boolean_ specifying the G zip. This is a required input.

**`bIdeas`**
: A _Boolean_ specifying the ideas. This is a required input.

**`bNLResult`**
: A _Boolean_ specifying the n l result. This is a required input.

**`iNLStepType`**
: An _Integer_ specifying the n l step type. This is a required input.

**`dEquiStart`**
: A _Double_ specifying the equi start. This is a required input.

**`dEquiStep`**
: A _Double_ specifying the equi step. This is a required input.

**`dEquiEnd`**
: A _Double_ specifying the equi end. This is a required input.

**`strNLStepList`**
: A _String_ specifying the n l step list. This is a required input.

**`bTimeStep`**
: A _Boolean_ specifying the time step. This is a required input.

**`iTimeStepKind`**
: An _Integer_ specifying the time step kind. This is a required input.

**`dTimeStart`**
: A _Double_ specifying the time start. This is a required input.

**`dTimeStep`**
: A _Double_ specifying the time step. This is a required input.

**`dTimeEnd`**
: A _Double_ specifying the time end. This is a required input.

**`iLCId`**
: An _Integer_ specifying the LC ID. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.Permas.Job(strName, strDescription, iType, crEdit, crlTarget, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
```
