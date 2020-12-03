```{module} Geometry.MergeEntities.Parts()
:synopsis: Merge Part
```

(Geometry.MergeEntities.Parts)=

# Geometry.MergeEntities.Parts

## Description

Merge Part

## Syntax

```python
Geometry.MergeEntities.Parts(dTolerance=1e-5, bRemovesharefaceflag=True, crlPart=[])
```

Macro: {ref}`Macro-Geometry-MergePart`

Ribbon: {menuselection}`Geometry --> MergeEntities --> Parts`

## Inputs

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 1e-5.

**`bRemovesharefaceflag`**
: A _Boolean_ specifying the removesharefaceflag. The default value is True.

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MergeEntities.Parts(dTolerance=1e-5, bRemovesharefaceflag=True, crlPart=[])
```
