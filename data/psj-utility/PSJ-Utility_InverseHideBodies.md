# InverseHideBodies

## Description

Inverse hide parts in view

## Inputs

1. id of part (int)

## Return Code

None

## Sample Code

```python
listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "Cube1", 1)
idbody = listbody[0].id
JPT.InverseHideBodies(idbody)
```
