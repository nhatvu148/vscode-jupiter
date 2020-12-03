```{module} Geometry.Transform.Position()
:synopsis: transform position
```

(Geometry.Transform.Position)=

# Geometry.Transform.Position

## Description

transform position

## Syntax

```python
Geometry.Transform.Position(crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)
```

Macro: {ref}`Macro-Geometry-PositionBody`

Ribbon: {menuselection}`Geometry --> Transform --> Position`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`veclPoint`**
: A _Vector List_ specifying the point. The default value is [[0.0, 0.0, 0.0]].

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.Position(crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)
```
