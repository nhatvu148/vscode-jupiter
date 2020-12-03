# CastDItemToDElem

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to [DElem](./../data-type/item-class/Class_DElem.md) object

## Inputs

1. DItem object (DItem class)

## Return Code

DElem object (DElem class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.ELEM)
ditemObject = listDItemObject[0]
JPT.CastDItemToDElem(ditemObject)
```
