```{module} MeshCleanup.AutoCheck()
:synopsis: check meshing quality
```

(MeshCleanup.AutoCheck)=

# MeshCleanup.AutoCheck

## Description

check meshing quality

## Syntax

```python
MeshCleanup.AutoCheck(crlPart, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElem)
```

Macro: {ref}`Macro-MeshCleanup-CleanupAuto`

Ribbon: {menuselection}`MeshCleanup --> AutoCheck`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`iElemType`**
: An _Integer_ specifying the element type. This is a required input.

**`blCheckCondition`**
: A _Boolean List_ specifying the check condition. This is a required input.

**`blElemQuality`**
: A _Boolean List_ specifying the element quality. This is a required input.

**`dlLimitValue`**
: A _Double List_ specifying the limit value. This is a required input.

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.AutoCheck(crlPart, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElem)
```
