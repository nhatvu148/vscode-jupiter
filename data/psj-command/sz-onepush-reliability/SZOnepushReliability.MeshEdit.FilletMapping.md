```{module} SZOnepushReliability.MeshEdit.FilletMapping()
:synopsis: Fillet mapping
```

(SZOnepushReliability.MeshEdit.FilletMapping)=

# SZOnepushReliability.MeshEdit.FilletMapping

## Description

Fillet mapping

## Syntax

```python
SZOnepushReliability.MeshEdit.FilletMapping(crlPart, crlFace, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```

Macro: {ref}`Macro-SZOnepushReliability-SORFilletMapping`

Ribbon: {menuselection}`SZOnepushReliability --> MeshEdit --> FilletMapping`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`dMinRadius`**
: A _Double_ specifying the minimum radius. This is a required input.

**`dMaxRadius`**
: A _Double_ specifying the maximum radius. This is a required input.

**`dMinAngle`**
: A _Double_ specifying the minimum angle. This is a required input.

**`dMaxAngle`**
: A _Double_ specifying the maximum angle. This is a required input.

**`bConvex`**
: A _Boolean_ specifying the convex. This is a required input.

**`bConcave`**
: A _Boolean_ specifying the concave. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SZOnepushReliability.MeshEdit.FilletMapping(crlPart, crlFace, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```
