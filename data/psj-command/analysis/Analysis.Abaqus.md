```{module} Analysis.Abaqus()
:synopsis: abaqus exporting
```

(Analysis.Abaqus)=

# Analysis.Abaqus

## Description

abaqus exporting

## Syntax

```python
Analysis.Abaqus(strName, bRBE2toMPC=False, bRenameProcess=False, iCodeType=0, iSurfDefType=0, iUnit=0, iWriteType=0, strDescription="", crlStepSequence=[], crEdit=None, strlUserText=[], bExptNdEleGroups=False, bDeleteFloatingNodes=False, bExptFaceElemGroups2Surface=False, bLoadCase=False, bAutoAssignDummyProperty=True, crDummyMat=None, bOutputGeometryId=True)
```

Macro: {ref}`Macro-Analysis-CreateAbaqusJob`

Ribbon: {menuselection}`Analysis --> Abaqus`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`bRBE2toMPC`**
: A _Boolean_ specifying the r e2to MPC. The default value is False.

**`bRenameProcess`**
: A _Boolean_ specifying the rename process. The default value is False.

**`iCodeType`**
: An _Integer_ specifying the code type. The default value is 0.

**`iSurfDefType`**
: An _Integer_ specifying the surface definition type. The default value is 0.

**`iUnit`**
: An _Integer_ specifying the unit. The default value is 0.

**`iWriteType`**
: An _Integer_ specifying the write type. The default value is 0.

**`strDescription`**
: A _String_ specifying the description. The default value is "".

**`crlStepSequence`**
: A _Cursor List_ specifying the step sequence. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`strlUserText`**
: A _String List_ specifying the user text. The default value is [].

**`bExptNdEleGroups`**
: A _Boolean_ specifying the exeption nd element groups. The default value is False.

**`bDeleteFloatingNodes`**
: A _Boolean_ specifying the delete floating nodes. The default value is False.

**`bExptFaceElemGroups2Surface`**
: A _Boolean_ specifying the exeption face element groups2 surface. The default value is False.

**`bLoadCase`**
: A _Boolean_ specifying the load case. The default value is False.

**`bAutoAssignDummyProperty`**
: A _Boolean_ specifying the auto assign dummy property. The default value is True.

**`crDummyMat`**
: A _Cursor_ specifying the dummy material. The default value is None.

**`bOutputGeometryId`**
: A _Boolean_ specifying the output geometry ID. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.Abaqus(strName, bRBE2toMPC=False, bRenameProcess=False, iCodeType=0, iSurfDefType=0, iUnit=0, iWriteType=0, strDescription="", crlStepSequence=[], crEdit=None, strlUserText=[], bExptNdEleGroups=False, bDeleteFloatingNodes=False, bExptFaceElemGroups2Surface=False, bLoadCase=False, bAutoAssignDummyProperty=True, crDummyMat=None, bOutputGeometryId=True)
```
