# CastDItemToDBody

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to [DBody](./../data-type/item-class/Class_DBody.md) object

## Inputs

1. DItem object (DItem class)

## Return Code

DBody object (DBody class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.BODY)
ditemObject = listDItemObject[0]
dbodyObject = JPT.CastDItemToDBody(ditemObject)
print(s)
```
