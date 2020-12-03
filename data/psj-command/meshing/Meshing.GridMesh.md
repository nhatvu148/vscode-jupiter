```{module} Meshing.GridMesh()
:synopsis: Grid meshing
```

(Meshing.GridMesh)=

# Meshing.GridMesh

## Description

Grid meshing

## Syntax

```python
Meshing.GridMesh(listGridMesh, bLocalsetting=True)
```

Macro: {ref}`Macro-Meshing-MeshingLocalMeshingGridMesh`

Ribbon: {menuselection}`Meshing --> GridMesh`

## Inputs

**`listGridMesh`**
: A _GRID_MESH List_ specifying the grid mesh. This is a required input.

**`bLocalsetting`**
: A _Boolean_ specifying the localsetting. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.GridMesh(listGridMesh, bLocalsetting=True)
```
