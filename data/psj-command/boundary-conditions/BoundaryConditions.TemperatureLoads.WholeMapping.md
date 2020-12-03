```{module} BoundaryConditions.TemperatureLoads.WholeMapping()
:synopsis: Create mapping pressure
```

(BoundaryConditions.TemperatureLoads.WholeMapping)=

# BoundaryConditions.TemperatureLoads.WholeMapping

## Description

Create mapping pressure

## Syntax

```python
BoundaryConditions.TemperatureLoads.WholeMapping(strName="TemperatureLoadsWholeMapping", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, iDScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodelBCMappingType=2, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="")
```

Macro: {ref}`Macro-BoundaryConditions-MappingTemperatureLoad`

Ribbon: {menuselection}`BoundaryConditions --> TemperatureLoads --> WholeMapping`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "TemperatureLoadsWholeMapping".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iMAPPos`**
: An _Integer_ specifying the m a p position. The default value is 0.

**`iViewCp`**
: An _Integer_ specifying the view component. The default value is 0.

**`iCp`**
: An _Integer_ specifying the component. The default value is 1.

**`iSrcType`**
: An _Integer_ specifying the source type. The default value is 0.

**`iMappedCpIndexArr0`**
: An _Integer_ specifying the mapped component index arr0. The default value is 0.

**`iMappedCpIndexArr1`**
: An _Integer_ specifying the mapped component index arr1. The default value is 0.

**`iDScaleFactor`**
: An _Integer_ specifying the d scale factor. The default value is 1.

**`posOffset`**
: A _Position_ specifying the offset. The default value is [0,0,0].

**`posRotate`**
: A _Position_ specifying the rotate. The default value is [0,0,0].

**`dCorScale`**
: A _Double_ specifying the cor scale. The default value is 1.

**`dSearchRange`**
: A _Double_ specifying the search range. The default value is 0.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iMappingMethod`**
: An _Integer_ specifying the mapping method. The default value is 0.

**`iSubmodelBCMappingType`**
: An _Integer_ specifying the submodel c mapping type. The default value is 2.

**`iMappingFromStepNo`**
: An _Integer_ specifying the mapping from step no. The default value is 0.

**`bSetADVCFile`**
: A _Boolean_ specifying the set ADVC file. The default value is False.

**`strADVCResultFile`**
: A _String_ specifying the ADVC result file. The default value is "".

**`bSetDetATol`**
: A _Boolean_ specifying the set det a tolerance. The default value is False.

**`dDetATol`**
: A _Double_ specifying the det a tolerance. The default value is DFLT_DBL.

**`bSetElementSet`**
: A _Boolean_ specifying the set element set. The default value is False.

**`strElementSet`**
: A _String_ specifying the element set. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.TemperatureLoads.WholeMapping(strName="TemperatureLoadsWholeMapping", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, iDScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodelBCMappingType=2, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="")
```
