```{module} Analysis.Analysis.Abaqus()
:synopsis: Unknown Description
```

(Analysis.Analysis.Abaqus)=

# Analysis.Analysis.Abaqus

## Description

Unknown Description

## Syntax

```python
Analysis.Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```

Macro: {ref}`Macro-Analysis-CreateAbaqusJob`

Ribbon: {menuselection}`Analysis --> Analysis --> Abaqus`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`bRBE2toMPC`**
: A _Boolean_ specifying the RBE2 to MPC. This is a required input.

**`bRenameProcess`**
: A _Boolean_ specifying the rename process. This is a required input.

**`iCodeType`**
: An _Integer_ specifying the code type. This is a required input.

**`iSurfDefType`**
: An _Integer_ specifying the surface definition type. This is a required input.

**`iUnit`**
: An _Integer_ specifying the unit. This is a required input.

**`iWriteType`**
: An _Integer_ specifying the write type. This is a required input.

**`strDescription`**
: A _String_ specifying the description. This is a required input.

**`crlStepSequence`**
: A _Cursor List_ specifying the step sequence. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

**`strlUserText`**
: A _String List_ specifying the user text. This is a required input.

**`bExptNdEleGroups`**
: A _Boolean_ specifying the exeption nd element groups. This is a required input.

**`bDeleteFloatingNodes`**
: A _Boolean_ specifying the delete floating nodes. This is a required input.

**`bExptFaceElemGroups2Surface`**
: A _Boolean_ specifying the exeption face element groups2 surface. This is a required input.

**`bLoadCase`**
: A _Boolean_ specifying the load case. This is a required input.

**`bAutoAssignDummyProperty`**
: A _Boolean_ specifying the auto assign dummy property. This is a required input.

**`crDummyMat`**
: A _Cursor_ specifying the dummy material. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```
