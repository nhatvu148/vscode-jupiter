```{module} Properties.PropertyTable()
:synopsis: renumber property/material ID
```

(Properties.PropertyTable)=

# Properties.PropertyTable

## Description

renumber property/material ID

## Syntax

```python
Properties.PropertyTable(listRenumberProp=[])
```

Macro: {ref}`Macro-Properties-RenumberPropertyTable`

Ribbon: {menuselection}`Properties --> PropertyTable`

## Inputs

**`listRenumberProp`**
: A _RENUMBER_PROP List_ specifying the renumber property. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.PropertyTable(listRenumberProp=[])
```
