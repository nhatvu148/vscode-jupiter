```{module} MeshCleanup.CorrectModel()
:synopsis: correct model
```

(MeshCleanup.CorrectModel)=

# MeshCleanup.CorrectModel

## Description

correct model

## Syntax

```python
MeshCleanup.CorrectModel(crlPart, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```

Macro: {ref}`Macro-MeshCleanup-CorrectModel`

Ribbon: {menuselection}`MeshCleanup --> CorrectModel`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`iEnableBreakEdge`**
: An _Integer_ specifying the enable break edge. The default value is 0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 0.

**`iEnableMergeEdge`**
: An _Integer_ specifying the enable merge edge. The default value is 0.

**`dMergeEdgeAngle`**
: A _Double_ specifying the merge edge angle. The default value is 0.

**`iEnableMergePlanarFace`**
: An _Integer_ specifying the enable merge planar face. The default value is 0.

**`iEnableRemoveExtraVertex`**
: An _Integer_ specifying the enable remove extra vertex. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.CorrectModel(crlPart, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```
