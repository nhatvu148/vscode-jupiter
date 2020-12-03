```{module} Properties.Solid()
:synopsis: create property solid
```

(Properties.Solid)=

# Properties.Solid

## Description

create property solid

## Syntax

```python
Properties.Solid(strName="Solid Property", iPID=1, crMaterial=None, iCordM=0, iIN=0, iOutLoc=0, iISOP=0, iFLflag=0, iModifiedElem=0, iModifiedElemADVC=0, bHasDynaRemesh=False, dDynaRemeshVal1=0.0, dDynaRemeshVal2=0.0, iAbaqusPropHGtype=0, dDispHG=0.0, crlTarget=[], crEdit=None, iFLG=0)
```

Macro: {ref}`Macro-Properties-Property3DSolid`

Ribbon: {menuselection}`Properties --> Solid`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Solid Property".

**`iPID`**
: An _Integer_ specifying the process ID. The default value is 1.

**`crMaterial`**
: A _Cursor_ specifying the material. The default value is None.

**`iCordM`**
: An _Integer_ specifying the coordinate m. The default value is 0.

**`iIN`**
: An _Integer_ specifying the increment. The default value is 0.

**`iOutLoc`**
: An _Integer_ specifying the outpu location. The default value is 0.

**`iISOP`**
: An _Integer_ specifying the ISOP. The default value is 0.

**`iFLflag`**
: An _Integer_ specifying the FL flag. The default value is 0.

**`iModifiedElem`**
: An _Integer_ specifying the modified element. The default value is 0.

**`iModifiedElemADVC`**
: An _Integer_ specifying the modified element ADVC. The default value is 0.

**`bHasDynaRemesh`**
: A _Boolean_ specifying the has dyna remesh. The default value is False.

**`dDynaRemeshVal1`**
: A _Double_ specifying the dyna remesh value 1. The default value is 0.0.

**`dDynaRemeshVal2`**
: A _Double_ specifying the dyna remesh value 2. The default value is 0.0.

**`iAbaqusPropHGtype`**
: An _Integer_ specifying the abaqus property HG type. The default value is 0.

**`dDispHG`**
: A _Double_ specifying the displacement HG. The default value is 0.0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iFLG`**
: An _Integer_ specifying the value FLG. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Solid(strName="Solid Property", iPID=1, crMaterial=None, iCordM=0, iIN=0, iOutLoc=0, iISOP=0, iFLflag=0, iModifiedElem=0, iModifiedElemADVC=0, bHasDynaRemesh=False, dDynaRemeshVal1=0.0, dDynaRemeshVal2=0.0, iAbaqusPropHGtype=0, dDispHG=0.0, crlTarget=[], crEdit=None, iFLG=0)
```
