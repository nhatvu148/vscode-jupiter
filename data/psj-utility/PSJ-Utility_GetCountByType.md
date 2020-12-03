# GetCountByType

## Description

Get count of entities by type

## Syntax

GetCountByType(JPT.DItemType.TYPE)

## Inputs

1. enum

DItem Type: BODY, VERTEX, EDGE, FACE, SOLID, ELEM,...

## Return Code

_Python Output_

- int

Number of entities

## Sample Code

_Input:_

```python
count = JPT.GetCountByType(JPT.DItemType.BODY)
print(str(count))
```

_Output:_

\> `2`
