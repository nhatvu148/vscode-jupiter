```{module} Analysis.TSSS.TransientHeatTransfer()
:synopsis: Export TS-SS Transient Heat Transfer
```

(Analysis.TSSS.TransientHeatTransfer)=

# Analysis.TSSS.TransientHeatTransfer

## Description

Export TS-SS Transient Heat Transfer

## Syntax

```python
Analysis.TSSS.TransientHeatTransfer(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)
```

Macro: {ref}`Macro-Analysis-TSSS_TransientHeatTransfer`

Ribbon: {menuselection}`Analysis --> TSSS --> TransientHeatTransfer`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Job_1".

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`nastranAnalysis`**
: A _NASTRAN_ANALYSIS_ specifying the nastran analysis data structure. The default value is NASTRAN_ANALYSIS().

**`iRadialReturn`**
: An _Integer_ specifying the radial return. The default value is 0.

**`listNastranNonlinear`**
: A _NASTRAN_NONLINEAR List_ specifying the nastran nonlinear. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`iModelCheckAnswer`**
: An _Integer_ specifying the model check answer. The default value is 0.

**`iDeleteSlaveNodesAnswer`**
: An _Integer_ specifying the delete slave nodes answer. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.TSSS.TransientHeatTransfer(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)
```
