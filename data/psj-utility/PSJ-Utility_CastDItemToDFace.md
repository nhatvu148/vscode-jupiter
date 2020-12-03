# CastDItemToDFace

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to [DFace](./../data-type/item-class/Class_DFace.md) object

## Inputs

1. DItem object (DItem class)

## Return Code

DFace object (DFace class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.FACE)
ditemObject = listDItemObject[0]
JPT.CastDItemToDFace(ditemObject)
```
