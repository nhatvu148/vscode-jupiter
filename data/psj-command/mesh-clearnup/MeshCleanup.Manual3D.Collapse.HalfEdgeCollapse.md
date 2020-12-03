```{module} MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse()
:synopsis: mash cleanup by manual for half edge collapse
```

(MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse)=

# MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse

## Description

mash cleanup by manual for half edge collapse

## Syntax

```python
MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse(crplElemEdge)
```

Macro: {ref}`Macro-MeshCleanup-CleanupHalfEdgeCollapse`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> Collapse --> HalfEdgeCollapse`

## Inputs

**`crplElemEdge`**
: A _Cursor Pair List_ specifying the element edge. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse(crplElemEdge)
```
