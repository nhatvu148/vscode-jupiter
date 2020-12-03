```{module} Analysis.ADVC.MakeProcess.SteadyState()
:synopsis: create advc heat transfer steady state process
```

(Analysis.ADVC.MakeProcess.SteadyState)=

# Analysis.ADVC.MakeProcess.SteadyState

## Description

create advc heat transfer steady state process

## Syntax

```python
Analysis.ADVC.MakeProcess.SteadyState(strName="", iEndType=1, dMaxTime=1, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[])
```

Macro: {ref}`Macro-Analysis-AdvcSSHProcess`

Ribbon: {menuselection}`Analysis --> ADVC --> MakeProcess --> SteadyState`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iEndType`**
: An _Integer_ specifying the end type. The default value is 1.

**`dMaxTime`**
: A _Double_ specifying the maximum time. The default value is 1.

**`iFixedOrAuto`**
: An _Integer_ specifying the fixed or auto. The default value is 0.

**`dMaxChange`**
: A _Double_ specifying the maximum change. The default value is DFLT_DBL.

**`dInitDt`**
: A _Double_ specifying the initial data. The default value is DFLT_DBL.

**`iDefineMaxDt`**
: An _Integer_ specifying the define maximum data. The default value is 0.

**`dMaxDt`**
: A _Double_ specifying the maximum data. The default value is DFLT_DBL.

**`iDefineMinDt`**
: An _Integer_ specifying the define minimum data. The default value is 0.

**`dMinDt`**
: A _Double_ specifying the minimum data. The default value is DFLT_DBL.

**`dFixedDt`**
: A _Double_ specifying the fixed data. The default value is DFLT_DBL.

**`iOutputLast`**
: An _Integer_ specifying the output last. The default value is -1.

**`iOutputInterval`**
: An _Integer_ specifying the output interval. The default value is DFLT_INT.

**`iRestartLast`**
: An _Integer_ specifying the restart last. The default value is -1.

**`iRestartInterval`**
: An _Integer_ specifying the restart interval. The default value is DFLT_INT.

**`dOutputTimeInterval`**
: A _Double_ specifying the output time interval. The default value is DFLT_DBL.

**`dRestartTimeInterval`**
: A _Double_ specifying the restart time interval. The default value is DFLT_DBL.

**`iOutputInit`**
: An _Integer_ specifying the output initial. The default value is -1.

**`iListOutputInterval`**
: An _Integer_ specifying the list output interval. The default value is DFLT_INT.

**`bConvergence`**
: A _Boolean_ specifying the convergence. The default value is False.

**`dCgTol`**
: A _Double_ specifying the cg tolerance. The default value is DFLT_DBL.

**`dCgNrTol`**
: A _Double_ specifying the cg nr tolerance. The default value is DFLT_DBL.

**`dCgDispTol`**
: A _Double_ specifying the cg displacement tolerance. The default value is DFLT_DBL.

**`dCgNrDispTol`**
: A _Double_ specifying the cg nr displacement tolerance. The default value is DFLT_DBL.

**`dCgDispLimitTol`**
: A _Double_ specifying the cg displacement limit tolerance. The default value is DFLT_DBL.

**`dCgTotalDispLimitTol`**
: A _Double_ specifying the cg total displacement limit tolerance. The default value is DFLT_DBL.

**`dNewtonTol`**
: A _Double_ specifying the newton tolerance. The default value is DFLT_DBL.

**`dNewtonDispTol`**
: A _Double_ specifying the newton displacement tolerance. The default value is DFLT_DBL.

**`dNewtonDispLimitTol`**
: A _Double_ specifying the newton displacement limit tolerance. The default value is DFLT_DBL.

**`dNewtonTotalDispLimitTol`**
: A _Double_ specifying the newton total displacement limit tolerance. The default value is DFLT_DBL.

**`iCgloopMax`**
: An _Integer_ specifying the cgloop maximum. The default value is DFLT_INT.

**`iNewtonMax`**
: An _Integer_ specifying the newton maximum. The default value is DFLT_INT.

**`dHtNlLoopTol`**
: A _Double_ specifying the ht nl loop tolerance. The default value is DFLT_DBL.

**`iHtNlLoopMax`**
: An _Integer_ specifying the ht nl loop maximum. The default value is DFLT_INT.

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

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ADVC.MakeProcess.SteadyState(strName="", iEndType=1, dMaxTime=1, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[])
```
