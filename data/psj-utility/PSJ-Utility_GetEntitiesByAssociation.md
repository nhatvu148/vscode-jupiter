# GetEntitiesByAssociation

## Description

Get list of entity object by association

## Inputs

1. DItem enum type (JPT.DItemType)

2. AssociateType type (JPT.AssociateType)

3. id entity (int)

## Return Code

list of DItem object (ItemVector)

## Sample Code

```python
JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS_BODY, 1)
```
