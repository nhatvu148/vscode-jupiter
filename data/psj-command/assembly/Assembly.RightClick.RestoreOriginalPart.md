```{module} Assembly.RightClick.RestoreOriginalPart()
:synopsis: Restore body
```

(Assembly.RightClick.RestoreOriginalPart)=

# Assembly.RightClick.RestoreOriginalPart

## Description

Restore body

## Syntax

```python
Assembly.RightClick.RestoreOriginalPart(crlBodies=[], bKeepShareFace=False)
```

Macro: {ref}`Macro-Assembly-RestoreBody`

Ribbon: {menuselection}`Assembly --> RightClick --> RestoreOriginalPart`

## Inputs

**`crlBodies`**
: A _Cursor List_ specifying the bodies. The default value is [].

**`bKeepShareFace`**
: A _Boolean_ specifying the keep share face. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.RestoreOriginalPart(crlBodies=[], bKeepShareFace=False)
```
