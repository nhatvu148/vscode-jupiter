# GetCenterOfEntities

## Description

Get center coordinate of selected entities

## Syntax

GetCenterOfEntities(vector DItem)

## Inputs

1. DItemVector

Vector DItem

## Return Code

_Python Output_

- DoubleVector

Coordinate\[x,y,z\] of selected entities

## Sample Code

_Input:_

```python
entity = JPT.GetAllSelected()
center = JPT.GetCenterOfEntities(entity)
for c in center:
    print(str(float(c)))
```

_Output:_

\> `0.004999999999999999`

\> `0.004999999999999999`

\> `0.010000000000000007`
