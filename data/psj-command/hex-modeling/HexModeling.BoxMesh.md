```{module} HexModeling.BoxMesh()
:synopsis: Box hex mesh creator for parts
```

(HexModeling.BoxMesh)=

# HexModeling.BoxMesh

## Description

Box hex mesh creator for parts

## Syntax

```python
HexModeling.BoxMesh(ilPartIds, dMeshSize, strMaterialName)
```

Macro: {ref}`Macro-HexModeling-HexBoxMesh`

Ribbon: {menuselection}`HexModeling --> BoxMesh`

## Inputs

**`ilPartIds`**
: A _Integer List_ specifying the part ids. This is a required input.

**`dMeshSize`**
: A _Double_ specifying the mesh size. This is a required input.

**`strMaterialName`**
: A _String_ specifying the material name. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.BoxMesh(ilPartIds, dMeshSize, strMaterialName)
```
