```{module} BoundaryConditions.LoadCase()
:synopsis: create load case
```

(BoundaryConditions.LoadCase)=

# BoundaryConditions.LoadCase

## Description

create load case

## Syntax

```python
BoundaryConditions.LoadCase(strName="LoadCase1", dFactor=1.0, crlTarget=[], iExportId=1, dlTargetFactor=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-LoadCase`

Ribbon: {menuselection}`BoundaryConditions --> LoadCase`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "LoadCase1".

**`dFactor`**
: A _Double_ specifying the factor. The default value is 1.0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iExportId`**
: An _Integer_ specifying the export ID. The default value is 1.

**`dlTargetFactor`**
: A _Double List_ specifying the target factor. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.LoadCase(strName="LoadCase1", dFactor=1.0, crlTarget=[], iExportId=1, dlTargetFactor=[], crEdit=None)
```
