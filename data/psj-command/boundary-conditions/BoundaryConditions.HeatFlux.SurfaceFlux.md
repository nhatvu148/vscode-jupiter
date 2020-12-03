```{module} BoundaryConditions.HeatFlux.SurfaceFlux()
:synopsis: create surface flux
```

(BoundaryConditions.HeatFlux.SurfaceFlux)=

# BoundaryConditions.HeatFlux.SurfaceFlux

## Description

create surface flux

## Syntax

```python
BoundaryConditions.HeatFlux.SurfaceFlux(strName, dFflux, iDistributionMethod, crTable, crlTarget, crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-SurfaceFlux`

Ribbon: {menuselection}`BoundaryConditions --> HeatFlux --> SurfaceFlux`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`dFflux`**
: A _Double_ specifying the fflux. This is a required input.

**`iDistributionMethod`**
: An _Integer_ specifying the distribution method. This is a required input.

**`crTable`**
: A _Cursor_ specifying the table. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.HeatFlux.SurfaceFlux(strName, dFflux, iDistributionMethod, crTable, crlTarget, crEdit=None)
```
