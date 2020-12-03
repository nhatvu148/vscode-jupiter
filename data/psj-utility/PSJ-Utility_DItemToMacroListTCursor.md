# DItemToMacroListTCursor

## Description

Convert a DItem object to cursor list macro string

## Inputs

1. DItem objects (DItem class)

## Return Code

cursor list macro string (string)

## Sample Code

```python
listnode = JPT.GetEntitiesByID(JPT.DItemType.NODE, 434)
node = JPT.DItemToMacroTCursor(listnode[0]) # 10:1
JPT.DItemToMacroListTCursor(node) # [10:1]
```
