# GetAllEdges

## Description

Get information of edges

## Syntax

GetAllEdges()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- EdgeVector

Edge information (id, key, typeID)

## Sample Code

_Input:_

```python
edges= JPT.GetAllEdges()
for ed in edges:
    print(str(ed.typeID)+' '+str(ed.id)+' '+str(ed.key))
```

_Output:_

\> `5 35 35`

\> `5 18 18`

\> `5 36 36`

\> `...`
