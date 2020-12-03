```{module} BoundaryConditions.EnforcedLoads.Velocity()
:synopsis: create enforced velocity
```

(BoundaryConditions.EnforcedLoads.Velocity)=

# BoundaryConditions.EnforcedLoads.Velocity

## Description

create enforced velocity

## Syntax

```python
BoundaryConditions.EnforcedLoads.Velocity(strName="EnforcedVelocity1", iDwDof=0, dFVel0=DFLT_DBL, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, iVelUnit=0, iRotUnit=0, bExport=False, crExportData0=None, crExportData1=None, crExportData2=None, crExportData3=None, crExportData4=None, crExportData5=None, crlTarget=[], crEdit=None, bADVCStatic=False)
```

Macro: {ref}`Macro-BoundaryConditions-EnforcedVelocity`

Ribbon: {menuselection}`BoundaryConditions --> EnforcedLoads --> Velocity`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "EnforcedVelocity1".

**`iDwDof`**
: An _Integer_ specifying the dw dof. The default value is 0.

**`dFVel0`**
: A _Double_ specifying the vel0. The default value is DFLT_DBL.

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

**`iVelUnit`**
: An _Integer_ specifying the vel unit. The default value is 0.

**`iRotUnit`**
: An _Integer_ specifying the rotation unit. The default value is 0.

**`bExport`**
: A _Boolean_ specifying the export. The default value is False.

**`crExportData0`**
: A _Cursor_ specifying the export data0. The default value is None.

**`crExportData1`**
: A _Cursor_ specifying the export data1. The default value is None.

**`crExportData2`**
: A _Cursor_ specifying the export data2. The default value is None.

**`crExportData3`**
: A _Cursor_ specifying the export data3. The default value is None.

**`crExportData4`**
: A _Cursor_ specifying the export data4. The default value is None.

**`crExportData5`**
: A _Cursor_ specifying the export data5. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bADVCStatic`**
: A _Boolean_ specifying the ADVC static. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.EnforcedLoads.Velocity(strName="EnforcedVelocity1", iDwDof=0, dFVel0=DFLT_DBL, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, iVelUnit=0, iRotUnit=0, bExport=False, crExportData0=None, crExportData1=None, crExportData2=None, crExportData3=None, crExportData4=None, crExportData5=None, crlTarget=[], crEdit=None, bADVCStatic=False)
```
