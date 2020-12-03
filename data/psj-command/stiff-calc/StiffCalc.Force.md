```{module} StiffCalc.Force()
:synopsis: create NormalUnityForce
```

(StiffCalc.Force)=

# StiffCalc.Force

## Description

create NormalUnityForce

## Syntax

```python
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTarget, crEdit)
```

Macro: {ref}`Macro-StiffCalc-PermasForce`

Ribbon: {menuselection}`StiffCalc --> Force`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`poslForce`**
: A _Position List_ specifying the force. This is a required input.

**`poslMoment`**
: A _Position List_ specifying the moment. This is a required input.

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. This is a required input.

**`iDistributionMethod`**
: An _Integer_ specifying the distribution method. This is a required input.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. This is a required input.

**`crTable`**
: A _Cursor_ specifying the table. This is a required input.

**`crNodeSet`**
: A _Cursor_ specifying the node set. This is a required input.

**`dFPhase`**
: A _Double_ specifying the phase. This is a required input.

**`dFDelay`**
: A _Double_ specifying the delay. This is a required input.

**`crPhaseTable`**
: A _Cursor_ specifying the phase table. This is a required input.

**`strFormula0`**
: A _String_ specifying the formula0. This is a required input.

**`strFormula1`**
: A _String_ specifying the formula1. This is a required input.

**`strFormula2`**
: A _String_ specifying the formula2. This is a required input.

**`strFormula3`**
: A _String_ specifying the formula3. This is a required input.

**`strFormula4`**
: A _String_ specifying the formula4. This is a required input.

**`strFormula5`**
: A _String_ specifying the formula5. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
StiffCalc.Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTarget, crEdit)
```
