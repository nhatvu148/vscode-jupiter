```{module} Properties.Material.Modify()
:synopsis: Unknown Description
```

(Properties.Material.Modify)=

# Properties.Material.Modify

## Description

Unknown Description

## Syntax

```python
Properties.Material.Modify(strMaterialID, listMaterialProperty)
```

Macro: {ref}`Macro-Properties-CreateMaterial`

Ribbon: {menuselection}`Properties --> Material --> Modify`

## Inputs

**`strMaterialID`**
: A _String_ specifying the material ID. This is a required input.

**`listMaterialProperty`**
: A _MATERIAL_PROPERTY List_ specifying the material property. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Material.Modify(strMaterialID, listMaterialProperty)
```
