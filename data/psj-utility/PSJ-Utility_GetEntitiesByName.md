# GetEntitiesByName

## Description

Get list of object entity by name

## Inputs

1. DTableType enum type (JPT.DItemType)

2. name of entity (string)

3. match with name option (1,0 or JPT.BoolType)

## Return Code

list of object entity (ItemVector)

## Sample Code

```python
listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "Cube1", 1)
```
