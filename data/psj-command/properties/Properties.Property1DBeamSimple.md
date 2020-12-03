```{module} Properties.Property1DBeamSimple()
:synopsis:
```

(Properties.Property1DBeamSimple)=

# Properties.Property1DBeamSimple

## Description

## Syntax

```python
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Properties-Property1DBeamSimple`

Ribbon: {menuselection}`Properties --> Property1DBeamSimple`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`iId`**
: An _Integer_ specifying the ID. This is a required input.

**`crSection`**
: A _Cursor_ specifying the section. The default value is None.

**`crMat`**
: A _Cursor_ specifying the material. The default value is None.

**`vecOrient`**
: A _Vector_ specifying the orient. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTarget=[], crEdit=None)
```
