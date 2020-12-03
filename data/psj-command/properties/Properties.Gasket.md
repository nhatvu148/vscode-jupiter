```{module} Properties.Gasket()
:synopsis: create property 3d gasket
```

(Properties.Gasket)=

# Properties.Gasket

## Description

create property 3d gasket

## Syntax

```python
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTarget, crEdit=None, iStData=0, iFLG=0)
```

Macro: {ref}`Macro-Properties-Prop3DGasket`

Ribbon: {menuselection}`Properties --> Gasket`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`crMaterial`**
: A _Cursor_ specifying the material. This is a required input.

**`dThickX`**
: A _Double_ specifying the thickness x. This is a required input.

**`dThickY`**
: A _Double_ specifying the thickness y. This is a required input.

**`dThickZ`**
: A _Double_ specifying the thickness z. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iStData`**
: An _Integer_ specifying the st data. The default value is 0.

**`iFLG`**
: An _Integer_ specifying the value FLG. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTarget, crEdit=None, iStData=0, iFLG=0)
```
