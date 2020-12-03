```{module} BoundaryConditions.LbcContactConvert()
:synopsis: BoundaryConditions LbcContactConvert
```

(BoundaryConditions.LbcContactConvert)=

# BoundaryConditions.LbcContactConvert

## Description

BoundaryConditions LbcContactConvert

## Syntax

```python
BoundaryConditions.LbcContactConvert(iConvertTo, iTieConvType, crlTarget)
```

Macro: {ref}`Macro-BoundaryConditions-LbcContactConvertTo`

Ribbon: {menuselection}`BoundaryConditions --> LbcContactConvert`

## Inputs

**`iConvertTo`**
: An _Integer_ specifying the convert to. This is a required input.

**`iTieConvType`**
: An _Integer_ specifying the tie conv type. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.LbcContactConvert(iConvertTo, iTieConvType, crlTarget)
```
