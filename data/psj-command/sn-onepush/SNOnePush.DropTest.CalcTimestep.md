```{module} SNOnePush.DropTest.CalcTimestep()
:synopsis: Used to calculate time step for drop test function
```

(SNOnePush.DropTest.CalcTimestep)=

# SNOnePush.DropTest.CalcTimestep

## Description

Used to calculate time step for drop test function

## Syntax

```python
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```

Macro: {ref}`Macro-SNOnePush-CalcTimeStep`

Ribbon: {menuselection}`SNOnePush --> DropTest --> CalcTimestep`

## Inputs

**`dRelevantElemRate`**
: A _Double_ specifying the relevant element rate. This is a required input.

**`dChangeMassRage`**
: A _Double_ specifying the change mass rage. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```
