```{module} Geometry.ShowAdjacent.Elements()
:synopsis: Unknown Description
```

(Geometry.ShowAdjacent.Elements)=

# Geometry.ShowAdjacent.Elements

## Description

Unknown Description

## Syntax

```python
Geometry.ShowAdjacent.Elements(dAngle=0.0, iIncludeStopElem=0, iLayer=1, bIsPreview=0, crlStartElem=[], crlStopElem=[])
```

Macro: {ref}`Macro-Geometry-Geom_ShowAdjacent_Elements`

Ribbon: {menuselection}`Geometry --> ShowAdjacent --> Elements`

## Inputs

**`dAngle`**
: A _Double_ specifying the angle stop. The default value is 0.0.

**`iIncludeStopElem`**
: An _Integer_ enable/disable option including stop element. The default value is 0.

**`iLayer`**
: An _Integer_ specifying the number of layer. This is a required input.

**`bIsPreview`**
: A _Boolean_ enable/disable option preview. The default value is False.

**`crlStartElem`**
: A _Cursor List_ specifying the list of start element. This is a required input.

**`crlStopElem`**
: A _Cursor List_ specifying the list of stop element. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.ShowAdjacent.Elements(dAngle=0.0, iIncludeStopElem=0, iLayer=1, bIsPreview=0, crlStarElem=[], crlStopElem=[])
```
