```{module} Assemble.Boolean()
:synopsis: Make Boolean between Parts
```

(Assemble.Boolean)=

# Assemble.Boolean

## Description

Make Boolean between Parts

## Syntax

```python
Assemble.Boolean(crlPart, iBooleanType=0, dToleranceAlignment=0.01, bLeaveOriginalBodies=False)
```

Macro: {ref}`Macro-Assemble-AssembleBoolean2`

Ribbon: {menuselection}`Assemble --> Boolean`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`iBooleanType`**
: An _Integer_ specifying the boolean type. The default value is 0.

**`dToleranceAlignment`**
: A _Double_ specifying the tolerance alignment. The default value is 0.01.

**`bLeaveOriginalBodies`**
: A _Boolean_ specifying the leave original bodies. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.Boolean(crlPart, iBooleanType=0, dToleranceAlignment=0.01, bLeaveOriginalBodies=False)
```
