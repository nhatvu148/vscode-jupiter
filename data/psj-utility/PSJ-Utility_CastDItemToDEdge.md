# CastDItemToDEdge

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to DEdge object

## Inputs

1. DItem object (DItem class)

## Return Code

DEdge object (DEdge class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.EDGE)
ditemObject = listDItemObject[0]
JPT.CastDItemToDEdge(ditemObject)
```
