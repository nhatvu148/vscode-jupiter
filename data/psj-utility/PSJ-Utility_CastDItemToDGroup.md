# CastDItemToDGroup

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to [DGroup](./../data-type/item-class/Class_DGroup.md) object

## Inputs

1. DItem object (DItem class)

## Return Code

DGroup object (DGroup class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.GROUP)
ditemObject = listDItemObject[0]
JPT.CastDItemToDGroup(ditemObject)
```
