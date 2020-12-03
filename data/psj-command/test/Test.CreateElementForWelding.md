```{module} Test.CreateElementForWelding()
:synopsis: Create weld elements
```

(Test.CreateElementForWelding)=

# Test.CreateElementForWelding

## Description

Create weld elements

## Syntax

```python
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlPart, crMaterial)
```

Macro: {ref}`Macro-Test-CreateElementForWelding`

Ribbon: {menuselection}`Test --> CreateElementForWelding`

## Inputs

**`crlSrcElems`**
: A _Cursor List_ specifying the source elems. This is a required input.

**`crlDstElems`**
: A _Cursor List_ specifying the dst elems. This is a required input.

**`crlSideElems`**
: A _Cursor List_ specifying the side elems. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crMaterial`**
: A _Cursor_ specifying the material. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlPart, crMaterial)
```
