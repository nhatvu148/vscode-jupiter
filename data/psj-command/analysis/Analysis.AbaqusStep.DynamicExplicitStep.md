```{module} Analysis.AbaqusStep.DynamicExplicitStep()
:synopsis: create abaqus step of abaqus dynamic explicit
```

(Analysis.AbaqusStep.DynamicExplicitStep)=

# Analysis.AbaqusStep.DynamicExplicitStep

## Description

create abaqus step of abaqus dynamic explicit

## Syntax

```python
Analysis.AbaqusStep.DynamicExplicitStep(strName, strDesp="", iEnableAutomatic=1, iIncrmtEstimator=0, abaqusPair1=ABAQUS_PAIR(), dTimeScalfactor=1.0, abaqusPair2=ABAQUS_PAIR(), iEnableNlgeom=1, dTimePeriod=1.0, iEnableIncludeHeatEffect=0, dLinearBlkVisco=0.06, dQuadrBlkVisco=1.2, listAbaqusOutputRequest=[], crEdit=None)
```

Macro: {ref}`Macro-Analysis-AbaqusDynamicExplicitStep`

Ribbon: {menuselection}`Analysis --> AbaqusStep --> DynamicExplicitStep`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strDesp`**
: A _String_ specifying the description. The default value is "".

**`iEnableAutomatic`**
: An _Integer_ specifying the enable automatic. The default value is 1.

**`iIncrmtEstimator`**
: An _Integer_ specifying the increment estimator. The default value is 0.

**`abaqusPair1`**
: A _ABAQUS_PAIR1_ specifying the abaqus pair 1 data structure. The default value is ABAQUS_PAIR().

**`dTimeScalfactor`**
: A _Double_ specifying the time scalfactor. The default value is 1.0.

**`abaqusPair2`**
: A _ABAQUS_PAIR2_ specifying the abaqus pair 2 data structure. The default value is ABAQUS_PAIR().

**`iEnableNlgeom`**
: An _Integer_ specifying the enable nlgeom. The default value is 1.

**`dTimePeriod`**
: A _Double_ specifying the time period. The default value is 1.0.

**`iEnableIncludeHeatEffect`**
: An _Integer_ specifying the enable include heat effect. The default value is 0.

**`dLinearBlkVisco`**
: A _Double_ specifying the linear block visco. The default value is 0.06.

**`dQuadrBlkVisco`**
: A _Double_ specifying the quadro block visco. The default value is 1.2.

**`listAbaqusOutputRequest`**
: A _ABAQUS_OUTPUT_REQUEST List_ specifying the abaqus output request. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.AbaqusStep.DynamicExplicitStep(strName, strDesp="", iEnableAutomatic=1, iIncrmtEstimator=0, abaqusPair1=ABAQUS_PAIR(), dTimeScalfactor=1.0, abaqusPair2=ABAQUS_PAIR(), iEnableNlgeom=1, dTimePeriod=1.0, iEnableIncludeHeatEffect=0, dLinearBlkVisco=0.06, dQuadrBlkVisco=1.2, listAbaqusOutputRequest=[], crEdit=None)
```
