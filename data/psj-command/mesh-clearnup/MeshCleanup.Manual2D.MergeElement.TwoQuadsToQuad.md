```{module} MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad()
:synopsis: Merge two Quad elements into one Quad element
```

(MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad)=

# MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad

## Description

Merge two Quad elements into one Quad element

## Syntax

```python
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElem)
```

Macro: {ref}`Macro-MeshCleanup-MC_ManualCleanup_2QuadToQuad`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> MergeElement --> TwoQuadsToQuad`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElem)
```
