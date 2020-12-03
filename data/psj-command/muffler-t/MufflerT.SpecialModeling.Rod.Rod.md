```{module} MufflerT.SpecialModeling.Rod.Rod()
:synopsis: create rod
```

(MufflerT.SpecialModeling.Rod.Rod)=

# MufflerT.SpecialModeling.Rod.Rod

## Description

create rod

## Syntax

```python
MufflerT.SpecialModeling.Rod.Rod(crlNode, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```

Macro: {ref}`Macro-MufflerT-CreateRod`

Ribbon: {menuselection}`MufflerT --> SpecialModeling --> Rod --> Rod`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`dRadius`**
: A _Double_ specifying the radius. This is a required input.

**`iType`**
: An _Integer_ specifying the type. This is a required input.

**`dMeshSize`**
: A _Double_ specifying the mesh size. This is a required input.

**`dStartDist`**
: A _Double_ specifying the start dist. This is a required input.

**`dWeldDist`**
: A _Double_ specifying the weld dist. This is a required input.

**`iDivNumber`**
: An _Integer_ specifying the divide number. This is a required input.

**`dDeformWidth`**
: A _Double_ specifying the deformation width. This is a required input.

**`iTransitionElem`**
: An _Integer_ specifying the transition element. This is a required input.

**`dlPosDir`**
: A _Double List_ specifying the position direction. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MufflerT.SpecialModeling.Rod.Rod(crlNode, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```
