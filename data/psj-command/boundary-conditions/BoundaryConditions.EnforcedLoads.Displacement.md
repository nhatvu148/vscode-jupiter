```{module} BoundaryConditions.EnforcedLoads.Displacement()
:synopsis: create enforced displacement
```

(BoundaryConditions.EnforcedLoads.Displacement)=

# BoundaryConditions.EnforcedLoads.Displacement

## Description

create enforced displacement

## Syntax

```python
BoundaryConditions.EnforcedLoads.Displacement(strName="", iDwDof=0, dFDisp0=DFLT_DBL, dFDisp1=DFLT_DBL, dFDisp2=DFLT_DBL, dFDisp3=DFLT_DBL, dFDisp4=DFLT_DBL, dFDisp5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-EnforcedDisplacement`

Ribbon: {menuselection}`BoundaryConditions --> EnforcedLoads --> Displacement`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iDwDof`**
: An _Integer_ specifying the dw dof. The default value is 0.

**`dFDisp0`**
: A _Double_ specifying the disp0. The default value is DFLT_DBL.

**`dFDisp1`**
: A _Double_ specifying the disp1. The default value is DFLT_DBL.

**`dFDisp2`**
: A _Double_ specifying the disp2. The default value is DFLT_DBL.

**`dFDisp3`**
: A _Double_ specifying the disp3. The default value is DFLT_DBL.

**`dFDisp4`**
: A _Double_ specifying the disp4. The default value is DFLT_DBL.

**`dFDisp5`**
: A _Double_ specifying the disp5. The default value is DFLT_DBL.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. The default value is 0.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crNodeSet`**
: A _Cursor_ specifying the node set. The default value is None.

**`dFPhase`**
: A _Double_ specifying the phase. The default value is DFLT_DBL.

**`dFDelay`**
: A _Double_ specifying the delay. The default value is DFLT_DBL.

**`crPhaseTable`**
: A _Cursor_ specifying the phase table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.EnforcedLoads.Displacement(strName="", iDwDof=0, dFDisp0=DFLT_DBL, dFDisp1=DFLT_DBL, dFDisp2=DFLT_DBL, dFDisp3=DFLT_DBL, dFDisp4=DFLT_DBL, dFDisp5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, crlTarget=[], crEdit=None)
```
