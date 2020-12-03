```{module} Properties.Material.Add()
:synopsis: Unknown Description
```

(Properties.Material.Add)=

# Properties.Material.Add

## Description

Unknown Description

## Syntax

```python
Properties.Material.Add(strMaterialName, listMaterialProperty)
```

Macro: {ref}`Macro-Properties-CreateMaterial`

Ribbon: {menuselection}`Properties --> Material --> Add`

## Inputs

**`strMaterialName`**
: A _String_ specifying the material name. This is a required input.

**`listMaterialProperty`**
: A _MATERIAL_PROPERTY List_ specifying the material property. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Material.Add(strMaterialName, listMaterialProperty)
```
