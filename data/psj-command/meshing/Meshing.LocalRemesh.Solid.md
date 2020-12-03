```{module} Meshing.LocalRemesh.Solid()
:synopsis:
```

(Meshing.LocalRemesh.Solid)=

# Meshing.LocalRemesh.Solid

## Description

## Syntax

```python
Meshing.LocalRemesh.Solid(crlPart=[], dlCenter=[0.0,0.0,0.0], dRadius=5.0, dGradFactor=1.0, dStrechLimit=0.1)
```

Macro: {ref}`Macro-Meshing-LocalRemeshSolid`

Ribbon: {menuselection}`Meshing --> LocalRemesh --> Solid`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dlCenter`**
: A _Double List_ specifying the center. The default value is [0.0,0.0,0.0].

**`dRadius`**
: A _Double_ specifying the radius. The default value is 5.0.

**`dGradFactor`**
: A _Double_ specifying the gradient factor. The default value is 1.0.

**`dStrechLimit`**
: A _Double_ specifying the strech limit. The default value is 0.1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalRemesh.Solid(crlPart=[], dlCenter=[0.0,0.0,0.0], dRadius=5.0, dGradFactor=1.0, dStrechLimit=0.1)
```
