# GetSelectedGroups

## Description

Get selected group information (Entity information inside group)

## Syntax

GetSelectedGroups()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- GroupVector

Selected group information ( id, key, name, targets, typeID)

## Sample Code

_Input:_

```python
groups=JPT.GetSelectedGroups()
for g in groups:
    for e in g.targets:
        print(str(e.typeID)+' '+str(e.id)+' '+str(e.key)+' '+str(e.name))
```

_Output:_

\> `3 2 2 Cylinder_1`

\> `3 1 1 Cube_1`
