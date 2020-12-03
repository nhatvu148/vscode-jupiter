# DItemListToMacroListTCursor

## Description

Convert list of DItem objects to cursor list macro string

## Inputs

1. list of DItem objects (ItemVector)

## Return Code

cursor list macro string (string)

## Sample Code

```python
listface1 = JPT.GetAllFaces()
JPT.DItemListToMacroListTCursor(listface1) # [10:1, 10:1, ...]
```
