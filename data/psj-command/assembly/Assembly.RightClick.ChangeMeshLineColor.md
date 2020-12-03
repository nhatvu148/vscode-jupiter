```{module} Assembly.RightClick.ChangeMeshLineColor()
:synopsis: Change Entity color
```

(Assembly.RightClick.ChangeMeshLineColor)=

# Assembly.RightClick.ChangeMeshLineColor

## Description

Change Entity color

## Syntax

```python
Assembly.RightClick.ChangeMeshLineColor(crlFace, iColor=0)
```

Macro: {ref}`Macro-Assembly-ChangeFaceMeshLineColor`

Ribbon: {menuselection}`Assembly --> RightClick --> ChangeMeshLineColor`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.ChangeMeshLineColor(crlFace, iColor=0)
```
