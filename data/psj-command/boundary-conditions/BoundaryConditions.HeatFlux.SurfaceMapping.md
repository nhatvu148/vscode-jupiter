```{module} BoundaryConditions.HeatFlux.SurfaceMapping()
:synopsis: Create mapping heat flux
```

(BoundaryConditions.HeatFlux.SurfaceMapping)=

# BoundaryConditions.HeatFlux.SurfaceMapping

## Description

Create mapping heat flux

## Syntax

```python
BoundaryConditions.HeatFlux.SurfaceMapping(strName="MappingHeatFlux", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strStrpath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=4, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")
```

Macro: {ref}`Macro-BoundaryConditions-MappingHeatFlux`

Ribbon: {menuselection}`BoundaryConditions --> HeatFlux --> SurfaceMapping`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "MappingHeatFlux".

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

**`dScaleFactor`**
: A _Double_ specifying the scale factor. The default value is 1.

**`posOffset`**
: A _Position_ specifying the offset. The default value is [0,0,0].

**`posRotate`**
: A _Position_ specifying the rotate. The default value is [0,0,0].

**`dCorScale`**
: A _Double_ specifying the cor scale. The default value is 1.

**`dSearchRange`**
: A _Double_ specifying the search range. The default value is 0.

**`iUnit`**
: An _Integer_ specifying the unit. The default value is 0.

**`strStrpath`**
: A _String_ specifying the strpath. The default value is "".

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iMappingMethod`**
: An _Integer_ specifying the mapping method. The default value is 0.

**`iSubmodeLBCMappingType`**
: An _Integer_ specifying the submode load boundary condition mapping type. The default value is 4.

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
: A _String_ specifying the element set. The default value is "all".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.HeatFlux.SurfaceMapping(strName="MappingHeatFlux", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strStrpath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=4, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")
```
