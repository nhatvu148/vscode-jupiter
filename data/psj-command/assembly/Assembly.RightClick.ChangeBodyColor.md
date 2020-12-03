```{module} Assembly.RightClick.ChangeBodyColor()
:synopsis: Change Body Color
```

(Assembly.RightClick.ChangeBodyColor)=

# Assembly.RightClick.ChangeBodyColor

## Description

Change Body Color

## Syntax

```python
Assembly.RightClick.ChangeBodyColor(listPartColorPair=[], bResetFaceColor=False)
```

Macro: {ref}`Macro-Assembly-ChangeBodyColor`

Ribbon: {menuselection}`Assembly --> RightClick --> ChangeBodyColor`

## Inputs

**`listPartColorPair`**
: A _PART_COLOR_PAIR List_ specifying the part color pair. The default value is [].

**`bResetFaceColor`**
: A _Boolean_ specifying the reset face color. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.ChangeBodyColor(listPartColorPair=[], bResetFaceColor=False)
```
