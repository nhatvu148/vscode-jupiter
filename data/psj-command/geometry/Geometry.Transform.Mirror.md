```{module} Geometry.Transform.Mirror()
:synopsis: mirror body
```

(Geometry.Transform.Mirror)=

# Geometry.Transform.Mirror

## Description

mirror body

## Syntax

```python
Geometry.Transform.Mirror(crlPart, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True, bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)
```

Macro: {ref}`Macro-Geometry-MirrorBody`

Ribbon: {menuselection}`Geometry --> Transform --> Mirror`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`veclPoint`**
: A _Vector List_ specifying the point. The default value is [[0.0, 0.0, 0.0]].

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.0.

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is True.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

**`bRemoveDupFace`**
: A _Boolean_ specifying the remove dup face. The default value is True.

**`bMergeNode`**
: A _Boolean_ specifying the merge node. The default value is False.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 1e-05.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.Mirror(crlPart, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True, bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)
```
