```{module} Analysis.Nastran.ModalTransientResponse()
:synopsis: Export Nastran Modal Transient Response
```

(Analysis.Nastran.ModalTransientResponse)=

# Analysis.Nastran.ModalTransientResponse

## Description

Export Nastran Modal Transient Response

## Syntax

```python
Analysis.Nastran.ModalTransientResponse(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)
```

Macro: {ref}`Macro-Analysis-Nastran_ModalTransientResponse`

Ribbon: {menuselection}`Analysis --> Nastran --> ModalTransientResponse`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Job_1".

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`nastranAnalysis`**
: A _NASTRAN_ANALYSIS_ specifying the nastran analysis data structure. The default value is NASTRAN_ANALYSIS().

**`bDummyPropAutoAssign`**
: A _Boolean_ specifying the dummy property auto assign. The default value is False.

**`iDummyPropMaterialID`**
: An _Integer_ specifying the dummy property material ID. The default value is 0.

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
Analysis.Nastran.ModalTransientResponse(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)
```
