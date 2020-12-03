# ShowHideEntitiesByID

## Description

Show or hide an entity by id in view

## Inputs

1. DTable enum type (JPT.DTableType)

2. entity id (int)

3. show/hide option (1,0 or JPT.BoolType)

## Return Code

None

## Sample Code

- show a part

```python
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)
```

- hide a part

```python
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.FALSE_VAL)
```
