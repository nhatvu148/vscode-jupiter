```{module} Properties.Section.ModifyGeneral()
:synopsis: Unknown Description
```

(Properties.Section.ModifyGeneral)=

# Properties.Section.ModifyGeneral

## Description

Unknown Description

## Syntax

```python
Properties.Section.ModifyGeneral(strName="", crSection=None, iSecType=0, iGeneralType=0, dA=0, dB=0, dH=0, dT1=0, dT2=0, dT3=0, bTapered=False, dDaTap=0, dDbTap=0, dDhTap=0, dDt1Tap=0, dDt2Tap=0, dDt3Tap=0)
```

Macro: {ref}`Macro-Properties-Property1DSectionModify_General`

Ribbon: {menuselection}`Properties --> Section --> ModifyGeneral`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`crSection`**
: A _Cursor_ specifying the section. The default value is None.

**`iSecType`**
: An _Integer_ specifying the section type. The default value is 0.

**`iGeneralType`**
: An _Integer_ specifying the general type. The default value is 0.

**`dA`**
: A _Double_ specifying the a. The default value is 0.

**`dB`**
: A _Double_ specifying the b. The default value is 0.

**`dH`**
: A _Double_ specifying the h. The default value is 0.

**`dT1`**
: A _Double_ specifying the t1. The default value is 0.

**`dT2`**
: A _Double_ specifying the t2. The default value is 0.

**`dT3`**
: A _Double_ specifying the t3. The default value is 0.

**`bTapered`**
: A _Boolean_ specifying the tapered. The default value is False.

**`dDaTap`**
: A _Double_ specifying the a tapered. The default value is 0.

**`dDbTap`**
: A _Double_ specifying the b tapered. The default value is 0.

**`dDhTap`**
: A _Double_ specifying the h tapered. The default value is 0.

**`dDt1Tap`**
: A _Double_ specifying the t1 tapered. The default value is 0.

**`dDt2Tap`**
: A _Double_ specifying the t2 tapered. The default value is 0.

**`dDt3Tap`**
: A _Double_ specifying the t3 tapered. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Section.ModifyGeneral(strName="", crSection=None, iSecType=0, iGeneralType=0, dA=0, dB=0, dH=0, dT1=0, dT2=0, dT3=0, bTapered=False, dDaTap=0, dDbTap=0, dDhTap=0, dDt1Tap=0, dDt2Tap=0, dDt3Tap=0)
```
