# CastToDItem

## Description

Cast an entity object to [DItem](./../data-type/item-class/Class_DItem.md) object

## Inputs

1. any kind of objects (DBody, DFace, DElem, DEdge, DGroup, DNode, etc.)

## Return Code

DItem object (DItem class)

## Sample Code

```python
listDbodyObject = JPT.GetAllParts()
dbodyObject = listDbodyObject[0]
ditemObject = JPT.CastToDItem(dbodyObject)
```
