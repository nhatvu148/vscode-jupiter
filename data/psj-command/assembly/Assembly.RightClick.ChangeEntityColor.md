```{module} Assembly.RightClick.ChangeEntityColor()
:synopsis: Unknown Description
```

(Assembly.RightClick.ChangeEntityColor)=

# Assembly.RightClick.ChangeEntityColor

## Description

Unknown Description

## Syntax

```python
Assembly.RightClick.ChangeEntityColor(crlEntity, iColor=0)
```

Macro: {ref}`Macro-Assembly-ChangeEntityColor`

Ribbon: {menuselection}`Assembly --> RightClick --> ChangeEntityColor`

## Inputs

**`crlEntity`**
: A _Cursor List_ specifying the entity. This is a required input.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.ChangeEntityColor(crlEntity, iColor=0)
```
