```{module} MainWindow.RightClick.AssociatedPick()
:synopsis: pick associated entity
```

(MainWindow.RightClick.AssociatedPick)=

# MainWindow.RightClick.AssociatedPick

## Description

pick associated entity

## Syntax

```python
MainWindow.RightClick.AssociatedPick(crlInput, strTarget, strConnect="UNKNOWN")
```

Macro: {ref}`Macro-MainWindow-AssociatedPick`

Ribbon: {menuselection}`MainWindow --> RightClick --> AssociatedPick`

## Inputs

**`crlInput`**
: A _Cursor List_ specifying the input. This is a required input.

**`strTarget`**
: A _String_ specifying the target. This is a required input.

**`strConnect`**
: A _String_ specifying the connect. The default value is "UNKNOWN".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MainWindow.RightClick.AssociatedPick(crlInput, strTarget, strConnect="UNKNOWN")
```
