# GetSharedFaces

## Description

Get shared face information

## Syntax

GetSharedFaces(DItemVector DItems)

## Inputs

1. DItemVector

Vector DItem

## Return Code

_Python Output_

- DItemVector

Shared face information (typeID, id, key)

## Sample Code

_Input:_

```python
shareFace = JPT.GetAllSelected()
share = JPT.GetSharedFaces(shareFace)
for s in share:
    print('typeID="{0}", id="{1}", key="{2}"'.format(s.typeID, s.id, s.key))
```

_Output:_

\> `typeID="6", id="115", key="115"`
