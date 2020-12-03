```{module} Test.ZGeometryTest.IntersectionCheck()
:synopsis: Intersection check
```

(Test.ZGeometryTest.IntersectionCheck)=

# Test.ZGeometryTest.IntersectionCheck

## Description

Intersection check

## Syntax

```python
Test.ZGeometryTest.IntersectionCheck(crlPart, crlFace, crlElem, iType)
```

Macro: {ref}`Macro-Test-IntersectionCheckZGeom`

Ribbon: {menuselection}`Test --> ZGeometryTest --> IntersectionCheck`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`iType`**
: An _Integer_ specifying the type. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.ZGeometryTest.IntersectionCheck(crlPart, crlFace, crlElem, iType)
```
