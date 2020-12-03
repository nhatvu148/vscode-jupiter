```{module} Analysis.ADVC.MakeProcess.DynamicExplicit()
:synopsis: create ADVC dynamic explicit process.
```

(Analysis.ADVC.MakeProcess.DynamicExplicit)=

# Analysis.ADVC.MakeProcess.DynamicExplicit

## Description

create ADVC dynamic explicit process.

## Syntax

```python
Analysis.ADVC.MakeProcess.DynamicExplicit(strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), iLogMessageInterval=DFLT_INT, iLinearApproximation=-1, dBulkViscosityCoef1=DFLT_DBL, dBulkViscosityCoef2=DFLT_DBL, dMassScalingdt=DFLT_DBL, dDtScaleFactor=DFLT_DBL, dPenaltyScaleFactor=DFLT_DBL, iContactSearchInterval=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcDynamicExplicitProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> DynamicExplicit`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`iGeomNonlinear`**
: An _Integer_ specifying the geometry nonlinear. The default value is 0.

**`advcStructTimeStep`**
: A _ADVC_STRUCT_TIME_STEP_ specifying the struct time step. The default value is ADVC_STRUCT_TIME_STEP().

**`bConvergence`**
: A _Boolean_ specifying the convergence. The default value is False.

**`advcConvergence`**
: A _ADVC_CONVERGENCE_ specifying the convergence. The default value is ADVC_CONVERGENCE().

**`bContact`**
: A _Boolean_ specifying the contact. The default value is False.

**`advcContactIter`**
: A _ADVC_CONTACT_ITER_ specifying the contact iterator. The default value is ADVC_CONTACT_ITER().

**`bAutoIncrement`**
: A _Boolean_ specifying the auto increment. The default value is False.

**`advcAutoIncrement`**
: A _ADVC_AUTO_INCREMENT_ specifying the auto increment. The default value is ADVC_AUTO_INCREMENT().

**`iLogMessageInterval`**
: An _Integer_ specifying the log message interval. The default value is DFLT_INT.

**`iLinearApproximation`**
: An _Integer_ specifying the linear approximation. The default value is -1.

**`dBulkViscosityCoef1`**
: A _Double_ specifying the bulk viscosity coefficient 1. The default value is DFLT_DBL.

**`dBulkViscosityCoef2`**
: A _Double_ specifying the bulk viscosity coefficient 2. The default value is DFLT_DBL.

**`dMassScalingdt`**
: A _Double_ specifying the mass scalingdt. The default value is DFLT_DBL.

**`dDtScaleFactor`**
: A _Double_ specifying the data scale factor. The default value is DFLT_DBL.

**`dPenaltyScaleFactor`**
: A _Double_ specifying the penalty scale factor. The default value is DFLT_DBL.

**`iContactSearchInterval`**
: An _Integer_ specifying the contact search interval. The default value is DFLT_INT.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`listLoadNode`**
: A _LOAD_NODE List_ specifying the load node. The default value is [].

**`listLoadCaseNode`**
: A _LOAD_CASE_NODE List_ specifying the load case node. The default value is [].

**`listLoadNodeContact`**
: A _LOAD_NODE_CONTACT List_ specifying the load node contact. The default value is [].

**`ilOutputParamList`**
: A _Integer List_ specifying the output param list. The default value is [].

**`iRefType`**
: An _Integer_ specifying the reference type. The default value is -1.

**`strRefPath`**
: A _String_ specifying the reference path. The default value is "".

**`listAdvcRefStressResult`**
: A _ADVC_REF_STRESS_RESULT List_ specifying the advc reference stress result. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ADVC.MakeProcess.DynamicExplicit(strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), iLogMessageInterval=DFLT_INT, iLinearApproximation=-1, dBulkViscosityCoef1=DFLT_DBL, dBulkViscosityCoef2=DFLT_DBL, dMassScalingdt=DFLT_DBL, dDtScaleFactor=DFLT_DBL, dPenaltyScaleFactor=DFLT_DBL, iContactSearchInterval=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
