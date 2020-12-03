```{module} BoundaryConditions.Convection.SurfaceMapping()
:synopsis: Create load boundary condition of convection Surface Mapping
```

(BoundaryConditions.Convection.SurfaceMapping)=

# BoundaryConditions.Convection.SurfaceMapping

## Description

Create load boundary condition of convection Surface Mapping

## Syntax

```python
BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection1", crlTarget=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0, iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0, dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-MappingConvection`

Ribbon: {menuselection}`BoundaryConditions --> Convection --> SurfaceMapping`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "MappingConvection1".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iPos`**
: An _Integer_ specifying the position. The default value is 0.

**`iViewCp`**
: An _Integer_ specifying the component index that to be previewed. The default value is 0.

**`iCp`**
: An _Integer_ specifying the component. The default value is 0.

**`iSrcType`**
: An _Integer_ specifying the source type. The default value is 0.

**`iMappedCpIndex0`**
: An _Integer_ specifying the mapped component index0. The default value is 0.

**`iMappedCpIndex1`**
: An _Integer_ specifying the mapped component index1. The default value is 0.

**`dRScale`**
: A _Double_ specifying the rotation scale. The default value is 1.0.

**`posOffset`**
: A _Position_ specifying the offset. The default value is [0,0,0].

**`posAxis`**
: A _Position_ specifying the axis. The default value is [0,0,0].

**`dTScale`**
: A _Double_ specifying the translation scale. The default value is 1.0.

**`dSearchRange`**
: A _Double_ specifying the search range. The default value is 1.0.

**`iHTCUnit`**
: An _Integer_ specifying the HTC unit. The default value is 0.

**`iTempUnit`**
: An _Integer_ specifying the temperature unit. The default value is 0.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection1", crlTarget=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0, iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0, dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)
```
