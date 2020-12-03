```{module} EngReliability.SubModelBC()
:synopsis: create mapping forced displacement
```

(EngReliability.SubModelBC)=

# EngReliability.SubModelBC

## Description

create mapping forced displacement

## Syntax

```python
EngReliability.SubModelBC(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```

Macro: {ref}`Macro-EngReliability-MappingForcedDisplacement`

Ribbon: {menuselection}`EngReliability --> SubModelBC`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`iPos`**
: An _Integer_ specifying the position. This is a required input.

**`iViewCp`**
: An _Integer_ specifying the view component. This is a required input.

**`iCp`**
: An _Integer_ specifying the component. This is a required input.

**`iSrcType`**
: An _Integer_ specifying the source type. This is a required input.

**`iMappedCpIndexArr0`**
: An _Integer_ specifying the mapped component index arr0. This is a required input.

**`dScaleR`**
: A _Double_ specifying the scale r. This is a required input.

**`vecOffset`**
: A _Vector_ specifying the offset. This is a required input.

**`vecRotate`**
: A _Vector_ specifying the rotate. This is a required input.

**`dScaleT`**
: A _Double_ specifying the scale t. This is a required input.

**`strPath`**
: A _String_ specifying the path. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

**`iMappingMethod`**
: An _Integer_ specifying the mapping method. This is a required input.

**`iSubmodelBCMappingType`**
: An _Integer_ specifying the submodel c mapping type. This is a required input.

**`iMappingFromStepNo`**
: An _Integer_ specifying the mapping from step no. This is a required input.

**`bSetADVCFile`**
: A _Boolean_ specifying the set ADVC file. This is a required input.

**`strADVCResultFile`**
: A _String_ specifying the ADVC result file. This is a required input.

**`bSetDetATol`**
: A _Boolean_ specifying the set det a tolerance. This is a required input.

**`dDetATol`**
: A _Double_ specifying the det a tolerance. This is a required input.

**`bSetElementSet`**
: A _Boolean_ specifying the set element set. This is a required input.

**`strElementSet`**
: A _String_ specifying the element set. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
EngReliability.SubModelBC(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```
