# DItemToMacroTCursor

## Description

Convert a DItem object to cursor macro string

## Inputs

1. DItem object (DItem class)

## Return Code

cursor macro string (string)

## Sample Code

```python
listnode1 = JPT.GetEntitiesByID(JPT.DItemType.NODE, 435)
listnode2 = JPT.GetEntitiesByID(JPT.DItemType.NODE, 434)
node1 = JPT.DItemToMacroTCursor(listnode1[0]) # 10:1
node2 = JPT.DItemToMacroTCursor(listnode2[0]) # 10:2
JPT.Exec('Collapse({0}, {1})'.format(node1, node2))
```
