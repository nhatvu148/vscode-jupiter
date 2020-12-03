```{module} Properties.Cohesive()
:synopsis: create property 3d cohesive
```

(Properties.Cohesive)=

# Properties.Cohesive

## Description

create property 3d cohesive

## Syntax

```python
Properties.Cohesive(strName, crMaterial, iResponse, bSpecifyThick, dInitialThick, crlTarget, crEdit=None, iFLG=0, iId=0, iSolverType=0, iADVCResponseType=0, iADVCStackDir=0, iEnableADVCThickness=0, dADVCThickness=DFLT_DBL)
```

Macro: {ref}`Macro-Properties-Prop3DCohesive`

Ribbon: {menuselection}`Properties --> Cohesive`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`crMaterial`**
: A _Cursor_ specifying the material. This is a required input.

**`iResponse`**
: An _Integer_ specifying the response. This is a required input.

**`bSpecifyThick`**
: A _Boolean_ specifying the specify thickness. This is a required input.

**`dInitialThick`**
: A _Double_ specifying the initial thickness. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iFLG`**
: An _Integer_ specifying the value FLG. The default value is 0.

**`iId`**
: An _Integer_ specifying the ID. The default value is 0.

**`iSolverType`**
: An _Integer_ specifying the solver type. The default value is 0.

**`iADVCResponseType`**
: An _Integer_ specifying the ADVC response type. The default value is 0.

**`iADVCStackDir`**
: An _Integer_ specifying the ADVC stack direction. The default value is 0.

**`iEnableADVCThickness`**
: An _Integer_ specifying the enable ADVC thickness. The default value is 0.

**`dADVCThickness`**
: A _Double_ specifying the ADVC thickness. The default value is DFLT_DBL.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Cohesive(strName, crMaterial, iResponse, bSpecifyThick, dInitialThick, crlTarget, crEdit=None, iFLG=0, iId=0, iSolverType=0, iADVCResponseType=0, iADVCStackDir=0, iEnableADVCThickness=0, dADVCThickness=DFLT_DBL)
```
