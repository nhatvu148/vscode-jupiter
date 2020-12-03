```{module} Properties.Composite()
:synopsis: Create 2D Composite Material Shell Property
```

(Properties.Composite)=

# Properties.Composite

## Description

Create 2D Composite Material Shell Property

## Syntax

```python
Properties.Composite(strName="", iDFT=0, dGE=DFLT_DBL, iDLAM=0, crMat=None, dNSM=DFLT_DBL, iDPID=0, dSB=DFLT_DBL, iDSOUT=0, dTREF=DFLT_DBL, dZ0=DFLT_DBL, dZOFF=DFLT_DBL, crlTarget=[], crEdit=None, crDcrLocalCS=None, iDmatOrientType=0, vecDmatOrient=[DFLT_DBL, DFLT_DBL, DFLT_DBL])
```

Macro: {ref}`Macro-Properties-Create2DCompositeMaterialShellProperty`

Ribbon: {menuselection}`Properties --> Composite`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iDLAM`**
: An _Integer_ specifying the DLAM. The default value is 0.

**`dGE`**
: A _Double_ specifying the back ground e. The default value is DFLT_DBL.

**`iDLAM`**
: An _Integer_ specifying the DLAM. The default value is 0.

**`crMat`**
: A _Cursor_ specifying the material. The default value is None.

**`dNSM`**
: A _Double_ specifying the NSM. The default value is DFLT_DBL.

**`iDPID`**
: An _Integer_ specifying the process ID. The default value is 0.

**`dSB`**
: A _Double_ specifying the sb. The default value is DFLT_DBL.

**`iDSOUT`**
: An _Integer_ specifying the ds output. The default value is 0.

**`dTREF`**
: A _Double_ specifying the TREF. The default value is DFLT_DBL.

**`dZ0`**
: A _Double_ specifying the z0. The default value is DFLT_DBL.

**`dZOFF`**
: A _Double_ specifying the ZOFF. The default value is DFLT_DBL.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`crDcrLocalCS`**
: A _Cursor_ specifying the dcr local coordinate system. The default value is None.

**`iDmatOrientType`**
: An _Integer_ specifying the dmat orient type. The default value is 0.

**`vecDmatOrient`**
: A _Vector_ specifying the dmat orient. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Composite(strName="", iDFT=0, dGE=DFLT_DBL, iDLAM=0, crMat=None, dNSM=DFLT_DBL, iDPID=0, dSB=DFLT_DBL, iDSOUT=0, dTREF=DFLT_DBL, dZ0=DFLT_DBL, dZOFF=DFLT_DBL, crlTarget=[], crEdit=None, crDcrLocalCS=None, iDmatOrientType=0, vecDmatOrient=[DFLT_DBL, DFLT_DBL, DFLT_DBL])
```
