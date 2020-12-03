# GetSelectedEdges

## Description

Get all of selected edge information

## Syntax

GetSelectedEdges()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- EdgeVector

Selected edge information (typeID, id, key)

## Sample Code

_Input:_

```python
edges = JPT.GetSelectedEdges()
for e in edges:
    print(str(e.typeID)+' '+str(e.id)+' '+str(e.key))
```

_Output:_

\> `5 19 19`

\> `5 27 27`

\> `5 18 18`
