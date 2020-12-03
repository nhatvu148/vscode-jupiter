```{module} Properties.Rod()
:synopsis: create 1D rod property
```

(Properties.Rod)=

# Properties.Rod

## Description

create 1D rod property

## Syntax

```python
Properties.Rod(strName="", iId=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Properties-Property1DRod`

Ribbon: {menuselection}`Properties --> Rod`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iId`**
: An _Integer_ specifying the ID. The default value is 1.

**`crSection`**
: A _Cursor_ specifying the section. The default value is None.

**`crMat`**
: A _Cursor_ specifying the material. The default value is None.

**`dArea`**
: A _Double_ specifying the area. The default value is DFLT_DBL.

**`dTorConst`**
: A _Double_ specifying the tor const. The default value is DFLT_DBL.

**`dTorStressCoeff`**
: A _Double_ specifying the tor stress coeff. The default value is DFLT_DBL.

**`dNSM`**
: A _Double_ specifying the n s m. The default value is DFLT_DBL.

**`iLocalLengthUnit`**
: An _Integer_ specifying the local length unit. The default value is 0.

**`iLocalMassUnit`**
: An _Integer_ specifying the local mass unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Rod(strName="", iId=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None)
```
