```{module} BoundaryConditions.InsideHeatGeneration()
:synopsis: Create load boundary condition of inside heat generation
```

(BoundaryConditions.InsideHeatGeneration)=

# BoundaryConditions.InsideHeatGeneration

## Description

Create load boundary condition of inside heat generation

## Syntax

```python
BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InsideHeatGeneration`

Ribbon: {menuselection}`BoundaryConditions --> InsideHeatGeneration`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InsideHeatGeneration1".

**`dInsideFlux`**
: A _Double_ specifying the inside flux. The default value is DFLT_DBL.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)
```
