# RemoveEntitiesByID

## Description

Remove entities from model by id

## Inputs

1. DItem enum type (JPT.DItemType)

2. id of entity (int)

## Return Code

None

## Sample Code

```python
listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "Cube", JPT.BoolType.FALSE_VAL)
idbody = listbody[0].id
JPT.RemoveEntitiesByID(JPT.DItemType.BODY, idbody)
```
