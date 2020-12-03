```{module} Properties.Shell()
:synopsis: create shell property
```

(Properties.Shell)=

# Properties.Shell

## Description

create shell property

## Syntax

```python
Properties.Shell(strName="Shell Property", iPID=1, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, dMatOrient1=0.0, dMatOrient2=0.0, dMatOrient3=0.0, dThickness=1, dBendStiff=0.0, dThickRatio=0.5, dNSM=0.0, dFiberDist1=0.0, dFiberDist2=0.0, dPlateOff=0.0, iItgPts=0, iMatOrientType=0, crLocalCS=None, crlTarget=[], crEdit=None, iDuplicateOpt=0)
```

Macro: {ref}`Macro-Properties-Property2DShell`

Ribbon: {menuselection}`Properties --> Shell`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Shell Property".

**`iPID`**
: An _Integer_ specifying the p ID. The default value is 1.

**`crMatMembrane`**
: A _Cursor_ specifying the material membrane. The default value is None.

**`crMatBend`**
: A _Cursor_ specifying the material bend. The default value is None.

**`crMatShear`**
: A _Cursor_ specifying the material shear. The default value is None.

**`crMatCoupl`**
: A _Cursor_ specifying the material couple. The default value is None.

**`dMatOrient1`**
: A _Double_ specifying the material orient1. The default value is 0.0.

**`dMatOrient2`**
: A _Double_ specifying the material orient2. The default value is 0.0.

**`dMatOrient3`**
: A _Double_ specifying the material orient3. The default value is 0.0.

**`dThickness`**
: A _Double_ specifying the thickness. The default value is 1.

**`dBendStiff`**
: A _Double_ specifying the bend stiff. The default value is 0.0.

**`dThickRatio`**
: A _Double_ specifying the thickness ratio. The default value is 0.5.

**`dNSM`**
: A _Double_ specifying the n s m. The default value is 0.0.

**`dFiberDist1`**
: A _Double_ specifying the fiber distance 1. The default value is 0.0.

**`dFiberDist2`**
: A _Double_ specifying the fiber distance 2. The default value is 0.0.

**`dPlateOff`**
: A _Double_ specifying the plate off. The default value is 0.0.

**`iItgPts`**
: An _Integer_ specifying the itg pts. The default value is 0.

**`iMatOrientType`**
: An _Integer_ specifying the material orient type. The default value is 0.

**`crLocalCS`**
: A _Cursor_ specifying the local coordinate system. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iDuplicateOpt`**
: An _Integer_ specifying the duplicate opt. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Shell(strName="Shell Property", iPID=1, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, dMatOrient1=0.0, dMatOrient2=0.0, dMatOrient3=0.0, dThickness=1, dBendStiff=0.0, dThickRatio=0.5, dNSM=0.0, dFiberDist1=0.0, dFiberDist2=0.0, dPlateOff=0.0, iItgPts=0, iMatOrientType=0, crLocalCS=None, crlTarget=[], crEdit=None, iDuplicateOpt=0)
```
