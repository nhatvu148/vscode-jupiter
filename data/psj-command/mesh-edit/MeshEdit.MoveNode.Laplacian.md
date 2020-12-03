```{module} MeshEdit.MoveNode.Laplacian()
:synopsis:
```

(MeshEdit.MoveNode.Laplacian)=

# MeshEdit.MoveNode.Laplacian

## Description

## Syntax

```python
MeshEdit.MoveNode.Laplacian(crlTarget=[], iType=0, bWithCADFollow=False)
```

Macro: {ref}`Macro-MeshEdit-LaplacianSmooth`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> Laplacian`

## Inputs

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`bWithCADFollow`**
: A _Boolean_ specifying the with CAD follow. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.Laplacian(crlTarget=[], iType=0, bWithCADFollow=False)
```
