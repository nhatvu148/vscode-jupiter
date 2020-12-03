```{module} Assemble.FullLayer()
:synopsis: assemble full layer
```

(Assemble.FullLayer)=

# Assemble.FullLayer

## Description

assemble full layer

## Syntax

```python
Assemble.FullLayer(crPart, dLayerWidth=1.0, iLayer=1, bUsePyramid=False)
```

Macro: {ref}`Macro-Assemble-AssembleFullLayer`

Ribbon: {menuselection}`Assemble --> FullLayer`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`dLayerWidth`**
: A _Double_ specifying the layer width. The default value is 1.0.

**`iLayer`**
: An _Integer_ specifying the layer. The default value is 1.

**`bUsePyramid`**
: A _Boolean_ specifying the use pyramid. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.FullLayer(crPart, dLayerWidth=1.0, iLayer=1, bUsePyramid=False)
```
