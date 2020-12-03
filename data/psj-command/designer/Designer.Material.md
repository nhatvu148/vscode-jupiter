```{module} Designer.Material()
:synopsis: Unknown Description
```

(Designer.Material)=

# Designer.Material

## Description

Unknown Description

## Syntax

```python
Designer.Material(strMatName, strPropName, dThickness, crlTarget)
```

Macro: {ref}`Macro-Designer-Material2DForDesigner`

Ribbon: {menuselection}`Designer --> Material`

## Inputs

**`strMatName`**
: A _String_ specifying the material name. This is a required input.

**`strPropName`**
: A _String_ specifying the property name. This is a required input.

**`dThickness`**
: A _Double_ specifying the thickness. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Designer.Material(strMatName, strPropName, dThickness, crlTarget)
```
