```{module} Geometry.BodyCut.BySurface()
:synopsis: Cut body by surface
```

(Geometry.BodyCut.BySurface)=

# Geometry.BodyCut.BySurface

## Description

Cut body by surface

## Syntax

```python
Geometry.BodyCut.BySurface(crlPart, crCutter, bSplitOnly=False, bMakeSectionFace=True, bShareFace=False, bSeparateFace=False)
```

Macro: {ref}`Macro-Geometry-BodyCutBySurfaceS`

Ribbon: {menuselection}`Geometry --> BodyCut --> BySurface`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crCutter`**
: A _Cursor_ specifying the cutter. This is a required input.

**`bSplitOnly`**
: A _Boolean_ specifying the split only. The default value is False.

**`bMakeSectionFace`**
: A _Boolean_ specifying the make section face. The default value is True.

**`bShareFace`**
: A _Boolean_ specifying the share face. The default value is False.

**`bSeparateFace`**
: A _Boolean_ specifying the separate face. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BodyCut.BySurface(crlPart, crCutter, bSplitOnly=False, bMakeSectionFace=True, bShareFace=False, bSeparateFace=False)
```
