# GetSharedElements

## Description

Get shared element information

## Syntax

GetSharedElements(DItemVector DItems)

## Inputs

1. DItemVector

Vector DItem

## Return Code

_Python Output_

- DItemVector

Shared element information (type, typeID, id, info, key, masters, slave, targets, children, parent )

## Sample Code

_Input:_

```python
bodies = JPT.GetAllByType(JPT.DItemType.BODY)
share = JPT.GetSharedElements(bodies)
for s in share:
    print(str(s.id))
```

_Output:_

\> `1170`

\> `1255`

\> `1202`

\> `...`
