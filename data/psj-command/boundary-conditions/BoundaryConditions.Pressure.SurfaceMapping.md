```{module} BoundaryConditions.Pressure.SurfaceMapping()
:synopsis: Create mapping pressure
```

(BoundaryConditions.Pressure.SurfaceMapping)=

# BoundaryConditions.Pressure.SurfaceMapping

## Description

Create mapping pressure

## Syntax

```python
BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-MappingPressure`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> SurfaceMapping`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "MappingPressure".

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

**`iMappedCpIndexArr`**
: An _Integer_ specifying the mapped component index arr. The default value is 0.

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

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)
```
