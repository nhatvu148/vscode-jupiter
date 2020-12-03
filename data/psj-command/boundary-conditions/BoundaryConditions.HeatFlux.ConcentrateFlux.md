```{module} BoundaryConditions.HeatFlux.ConcentrateFlux()
:synopsis: Unknown Description
```

(BoundaryConditions.HeatFlux.ConcentrateFlux)=

# BoundaryConditions.HeatFlux.ConcentrateFlux

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", lbcConcentrateFluxData=LBC_CONCENTRATE_FLUX_DATA(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ConcentrateFlux`

Ribbon: {menuselection}`BoundaryConditions --> HeatFlux --> ConcentrateFlux`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ConcentrateHeatFlux1".

**`lbcConcentrateFluxData`**
: A _LBC_CONCENTRATE_FLUX_DATA_ specifying the concentrate flux data. The default value is LBC_CONCENTRATE_FLUX_DATA().

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", lbcConcentrateFluxData=LBC_CONCENTRATE_FLUX_DATA(), crlTarget=[], crEdit=None)
```
