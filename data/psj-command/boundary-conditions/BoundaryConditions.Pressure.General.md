```{module} BoundaryConditions.Pressure.General()
:synopsis: Create general pressure boundary condition
```

(BoundaryConditions.Pressure.General)=

# BoundaryConditions.Pressure.General

## Description

Create general pressure boundary condition

## Syntax

```python
BoundaryConditions.Pressure.General(strName="Pressure1", dFpressure=0.0, iIdistribute=0, crTable=None, dDphase=0.0, dDdelay=0.0, crPhaseTable=None, strFormularValue="", crCoord=None, dlDirection=[DFLT_DBL,DFLT_DBL,DFLT_DBL], strFormularDirX="", strFormularDirY="", strFormularDirZ="", iArrowDir=1, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-PressureGeneral`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> General`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Pressure1".

**`dFpressure`**
: A _Double_ specifying the fpressure. The default value is 0.0.

**`iIdistribute`**
: An _Integer_ specifying the idistribute. The default value is 0.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`dDphase`**
: A _Double_ specifying the dphase. The default value is 0.0.

**`dDdelay`**
: A _Double_ specifying the ddelay. The default value is 0.0.

**`crPhaseTable`**
: A _Cursor_ specifying the phase table. The default value is None.

**`strFormularValue`**
: A _String_ specifying the formular value. The default value is "".

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dlDirection`**
: A _Double List_ specifying the direction. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`strFormularDirX`**
: A _String_ specifying the formular direction x. The default value is "".

**`strFormularDirY`**
: A _String_ specifying the formular direction y. The default value is "".

**`strFormularDirZ`**
: A _String_ specifying the formular direction z. The default value is "".

**`iArrowDir`**
: An _Integer_ specifying the arrow direction. The default value is 1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.General(strName="Pressure1", dFpressure=0.0, iIdistribute=0, crTable=None, dDphase=0.0, dDdelay=0.0, crPhaseTable=None, strFormularValue="", crCoord=None, dlDirection=[DFLT_DBL,DFLT_DBL,DFLT_DBL], strFormularDirX="", strFormularDirY="", strFormularDirZ="", iArrowDir=1, crlTarget=[], crEdit=None)
```
