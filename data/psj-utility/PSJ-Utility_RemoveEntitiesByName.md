# RemoveEntitiesByName

## Description

Remove entities from model by name

## Inputs

1. DTable enum type (JPT.DTableType)

2. name of entity (string)

3. match with name option (1,0 or JPT.BoolType)

## Return Code

None

## Sample Code

```python
JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, "Cube_1", 1)
```
