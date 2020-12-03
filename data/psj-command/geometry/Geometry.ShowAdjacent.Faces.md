```{module} Geometry.ShowAdjacent.Faces()
:synopsis: Unknown Description
```

(Geometry.ShowAdjacent.Faces)=

# Geometry.ShowAdjacent.Faces

## Description

Unknown Description

## Syntax

```python
Geometry.ShowAdjacent.Faces(dAngle=0.0, iIncludeStopFace=0, iLayer=1, bIsPreview=0, crlStartFace=[] , crlStopFace=[])
```

Macro: {ref}`Macro-Geometry-Geom_ShowAdjacent`

Ribbon: {menuselection}`Geometry --> ShowAdjacent --> Faces`

## Inputs

**`dAngle`**
: A _Double_ specifying the angle stop. The default value is 0.0.

**`iIncludeStopFace`**
: An _Integer_ enable/disable option including stop face. The default value is 0.

**`iLayer`**
: An _Integer_ specifying the number of layer. This is a required input.

**`bIsPreview`**
: A _Boolean_ enable/disable option preview. The default value is False.

**`crlStartFace`**
: A _Cursor List_ specifying the list of start face. This is a required input.

**`crlStopFace`**
: A _Cursor List_ specifying the list of stop face. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.ShowAdjacent.Faces(dAngle=0.0, iIncludeStopFace=0, iLayer=1, bIsPreview=0, crlStartFace=[] , crlStopFace=[])
```
