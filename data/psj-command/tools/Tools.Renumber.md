```{module} Tools.Renumber()
:synopsis: Set renumber data
```

(Tools.Renumber)=

# Tools.Renumber

## Description

Set renumber data

## Syntax

```python
Tools.Renumber(listRenumberItem=[], bAssignProp=True, bSurfCornerFirst=False)
```

Macro: {ref}`Macro-Tools-RenumberE`

Ribbon: {menuselection}`Tools --> Renumber`

## Inputs

**`listRenumberItem`**
: A _RENUMBER_ITEM List_ specifying the renumber item. The default value is [].

**`bAssignProp`**
: A _Boolean_ specifying the assign property. The default value is True.

**`bSurfCornerFirst`**
: A _Boolean_ specifying the surface corner first. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Renumber(listRenumberItem=[], bAssignProp=True, bSurfCornerFirst=False)
```
