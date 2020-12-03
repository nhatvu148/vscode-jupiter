```{module} MeshEdit.Import()
:synopsis: Move nodes deformation
```

(MeshEdit.Import)=

# MeshEdit.Import

## Description

Move nodes deformation

## Syntax

```python
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```

Macro: {ref}`Macro-MeshEdit-MoveNodeDeform`

Ribbon: {menuselection}`MeshEdit --> Import`

## Inputs

**`iSolverType`**
: An _Integer_ specifying the solver type. The default value is 0.

**`strFilePath`**
: A _String_ specifying the file path. The default value is "".

**`iStep`**
: An _Integer_ specifying the step. The default value is 0.

**`dScale`**
: A _Double_ specifying the scale. The default value is 1.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```
