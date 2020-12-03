# GetSelectedNodes

## Description

Get selected node information

## Syntax

GetSelectedNodes()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- NodeVector

Selected node information (typeID, id, key, pos)

## Sample Code

_Input:_

```python
nodes= JPT.GetSelectedNodes()
for n in nodes:
    print('type="{0}", id="{1}", key="{2}"'.format(n.typeID, n.id, n.key))
```

_Output:_

\> `type="10", id="93", key="93"`

\> `type="10", id="486", key="486"`

\> `type="10", id="480", key="480"`
