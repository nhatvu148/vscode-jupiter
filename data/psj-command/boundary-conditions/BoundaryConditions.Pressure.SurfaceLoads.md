```{module} BoundaryConditions.Pressure.SurfaceLoads()
:synopsis: create distrubited pressure
```

(BoundaryConditions.Pressure.SurfaceLoads)=

# BoundaryConditions.Pressure.SurfaceLoads

## Description

create distrubited pressure

## Syntax

```python
BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[0,0,0], iArrowdir=0, crCoordinate=None, crlTargetFace=[], crEditCur=None)
```

Macro: {ref}`Macro-BoundaryConditions-SurfaceLoads`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> SurfaceLoads`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "SurfaceLoads1".

**`dlPressure`**
: A _Double List_ specifying the pressure. The default value is [0,0,0].

**`iArrowdir`**
: An _Integer_ specifying the arrowdir. The default value is 0.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. The default value is [].

**`crEditCur`**
: A _Cursor_ specifying the edit cur. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[0,0,0], iArrowdir=0, crCoordinate=None, crlTargetFace=[], crEditCur=None)
```
