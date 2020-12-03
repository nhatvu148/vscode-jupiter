```{module} BoundaryConditions.Force.General()
:synopsis: create force general
```

(BoundaryConditions.Force.General)=

# BoundaryConditions.Force.General

## Description

create force general

## Syntax

```python
BoundaryConditions.Force.General(strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], vecMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crTable=None, crNodeSet=None, dFPhase=0.0, dFDelay=0.0, crPhaseTable=None, strFormula1="", strFormula2="", strFormula3="", strFormula4="", strFormula5="", strFormula6="", crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ForceGeneral`

Ribbon: {menuselection}`BoundaryConditions --> Force --> General`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`vecForce`**
: A _Vector_ specifying the force. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

**`vecMoment`**
: A _Vector_ specifying the moment. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. The default value is 0.

**`iDistributionMethod`**
: An _Integer_ specifying the distribution method. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crNodeSet`**
: A _Cursor_ specifying the node set. The default value is None.

**`dFPhase`**
: A _Double_ specifying the phase. The default value is 0.0.

**`dFDelay`**
: A _Double_ specifying the delay. The default value is 0.0.

**`crPhaseTable`**
: A _Cursor_ specifying the phase table. The default value is None.

**`strFormula1`**
: A _String_ specifying the formula1. The default value is "".

**`strFormula2`**
: A _String_ specifying the formula2. The default value is "".

**`strFormula3`**
: A _String_ specifying the formula3. The default value is "".

**`strFormula4`**
: A _String_ specifying the formula4. The default value is "".

**`strFormula5`**
: A _String_ specifying the formula5. The default value is "".

**`strFormula6`**
: A _String_ specifying the formula6. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.General(strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], vecMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crTable=None, crNodeSet=None, dFPhase=0.0, dFDelay=0.0, crPhaseTable=None, strFormula1="", strFormula2="", strFormula3="", strFormula4="", strFormula5="", strFormula6="", crlTarget=[], crEdit=None)
```
