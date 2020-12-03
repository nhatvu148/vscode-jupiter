```{module} Analysis.ADVC.MakeProcess.Creep()
:synopsis: create creep process
```

(Analysis.ADVC.MakeProcess.Creep)=

# Analysis.ADVC.MakeProcess.Creep

## Description

create creep process

## Syntax

```python
Analysis.ADVC.MakeProcess.Creep(strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=DFLT_DBL, bThetaDefined=False, dTheta=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```

Macro: {ref}`Macro-Analysis-AdvcCreepProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> Creep`

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

**`dStabilizationFactor`**
: A _Double_ specifying the stabilization factor. The default value is DFLT_DBL.

**`bThetaDefined`**
: A _Boolean_ specifying the theta defined. The default value is False.

**`dTheta`**
: A _Double_ specifying the theta. The default value is DFLT_DBL.

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
Analysis.ADVC.MakeProcess.Creep(strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=DFLT_DBL, bThetaDefined=False, dTheta=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
