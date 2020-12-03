```{module} BoundaryConditions.Submodel.SubmodelForcedFlux()
:synopsis: create submodel forced flux
```

(BoundaryConditions.Submodel.SubmodelForcedFlux)=

# BoundaryConditions.Submodel.SubmodelForcedFlux

## Description

create submodel forced flux

## Syntax

```python
BoundaryConditions.Submodel.SubmodelForcedFlux(strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-SubmodelForcedFlux`

Ribbon: {menuselection}`BoundaryConditions --> Submodel --> SubmodelForcedFlux`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`iSolver`**
: An _Integer_ specifying the solver. The default value is 0.

**`strFilePathName`**
: A _String_ specifying the file path name. The default value is "/home/".

**`iProcessNo`**
: An _Integer_ specifying the process no. The default value is 0.

**`iReferType`**
: An _Integer_ specifying the refer type. The default value is -1.

**`dExtensionRange`**
: A _Double_ specifying the extension range. The default value is DFLT_DBL.

**`dExtensionTol`**
: A _Double_ specifying the extension tolerance. The default value is DFLT_DBL.

**`dExtensionLimitTol`**
: A _Double_ specifying the extension limit tolerance. The default value is DFLT_DBL.

**`strGlobalElementSet`**
: A _String_ specifying the global element set. The default value is "".

**`iUseBucket`**
: An _Integer_ specifying the use bucket. The default value is -1.

**`iNumBucketMaxX`**
: An _Integer_ specifying the number bucket maximum x. The default value is DFLT_INT.

**`iNumBucketMaxY`**
: An _Integer_ specifying the number bucket maximum y. The default value is DFLT_INT.

**`iNumBucketMaxZ`**
: An _Integer_ specifying the number bucket maximum z. The default value is DFLT_INT.

**`iPrevBc`**
: An _Integer_ specifying the prev bc. The default value is -1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Submodel.SubmodelForcedFlux(strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None)
```
