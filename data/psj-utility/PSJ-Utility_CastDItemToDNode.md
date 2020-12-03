# CastDItemToDNode

## Description

Cast a [DItem](./../data-type/item-class/Class_DItem.md) object to [DNode](./../data-type/item-class/Class_DNode.md) object

## Inputs

1. DItem object (DItem class)

## Return Code

DNode object (DNode class)

## Sample Code

```python
listDItemObject = JPT.GetAllByType(JPT.DItemType.NODE)
ditemObject = listDItemObject[0]
JPT.CastDItemToDNode(ditemObject)
```
