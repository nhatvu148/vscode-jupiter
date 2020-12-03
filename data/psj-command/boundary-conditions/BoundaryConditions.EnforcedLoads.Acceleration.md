```{module} BoundaryConditions.EnforcedLoads.Acceleration()
:synopsis: Set enforced acceleration
```

(BoundaryConditions.EnforcedLoads.Acceleration)=

# BoundaryConditions.EnforcedLoads.Acceleration

## Description

Set enforced acceleration

## Syntax

```python
BoundaryConditions.EnforcedLoads.Acceleration(strName="EnforcedAcceleration1", iDwDof=0, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, dFVel6=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, bExport=False, crMEExport1=None, crMEExport2=None, crMEExport3=None, crMEExport4=None, crMEExport5=None, crMEExport6=None, iAcUnit=0, iRotUnit=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-EnforcedAcceleration`

Ribbon: {menuselection}`BoundaryConditions --> EnforcedLoads --> Acceleration`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "EnforcedAcceleration1".

**`iDwDof`**
: An _Integer_ specifying the dw dof. The default value is 0.

**`dFVel1`**
: A _Double_ specifying the vel1. The default value is DFLT_DBL.

**`dFVel2`**
: A _Double_ specifying the vel2. The default value is DFLT_DBL.

**`dFVel3`**
: A _Double_ specifying the vel3. The default value is DFLT_DBL.

**`dFVel4`**
: A _Double_ specifying the vel4. The default value is DFLT_DBL.

**`dFVel5`**
: A _Double_ specifying the vel5. The default value is DFLT_DBL.

**`dFVel6`**
: A _Double_ specifying the vel6. The default value is DFLT_DBL.

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

**`bExport`**
: A _Boolean_ specifying the export. The default value is False.

**`crMEExport1`**
: A _Cursor_ specifying the m e export1. The default value is None.

**`crMEExport2`**
: A _Cursor_ specifying the m e export2. The default value is None.

**`crMEExport3`**
: A _Cursor_ specifying the m e export3. The default value is None.

**`crMEExport4`**
: A _Cursor_ specifying the m e export4. The default value is None.

**`crMEExport5`**
: A _Cursor_ specifying the m e export5. The default value is None.

**`crMEExport6`**
: A _Cursor_ specifying the m e export6. The default value is None.

**`iAcUnit`**
: An _Integer_ specifying the ac unit. The default value is 0.

**`iRotUnit`**
: An _Integer_ specifying the rotation unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.EnforcedLoads.Acceleration(strName="EnforcedAcceleration1", iDwDof=0, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, dFVel6=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, bExport=False, crMEExport1=None, crMEExport2=None, crMEExport3=None, crMEExport4=None, crMEExport5=None, crMEExport6=None, iAcUnit=0, iRotUnit=0, crlTarget=[], crEdit=None)
```
