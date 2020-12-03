# GetAllByTypeID

## Description

Get information of entities by inputing their typeIDs

## Syntax

GetAllByTypeID(int iTypeID)

## Inputs

1. Int

Type ID of entities

## Return Code

_Python Output_

- DItemVector

Information of entities: id, name, info, isValid, key, masters, slaves, target, type, type ID, parent, children

## Sample Code

_Input:_

```python
typeid = JPT.GetAllByTypeID(3)
for t in typeid:
    print('Name: "{0}"; ID = {1}'.format(t.name, t.id))
```

_Output:_

\> `Name: "Pin"; ID = 1`

\> `Name: "plunger"; ID = 2`

\> `Name: "Base"; ID = 3`
