```{module} ACModeling.ACBoundary.FirstMethod()
:synopsis: Unknown Description
```

(ACModeling.ACBoundary.FirstMethod)=

# ACModeling.ACBoundary.FirstMethod

## Description

Unknown Description

## Syntax

```python
ACModeling.ACBoundary.FirstMethod(crlPart, bIsMergePart, bIsRenumber)
```

Macro: {ref}`Macro-ACModeling-ACBoundaryMethod1`

Ribbon: {menuselection}`ACModeling --> ACBoundary --> FirstMethod`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`bIsMergePart`**
: A _Boolean_ specifying the is merge part. This is a required input.

**`bIsRenumber`**
: A _Boolean_ specifying the is renumber. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
ACModeling.ACBoundary.FirstMethod(crlPart, bIsMergePart, bIsRenumber)
```
