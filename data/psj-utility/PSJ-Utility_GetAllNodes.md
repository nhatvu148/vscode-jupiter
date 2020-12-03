# GetAllNodes

## Description

Get information of all nodes

## Syntax

GetAllNodes()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- NodeVector

Node information (typeID, id, key, pos)

## Sample Code

_Input:_

```python
nodes= JPT.GetAllNodes()
for n in nodes:
    print('type="{0}", id="{1}", key="{2}"'.format(n.typeID, n.id, n.key))
```

_Output:_

\> `type="10", id="772", key="772"`

\> `type="10", id="251", key="251"`

\> `type="10", id="609", key="609"`

\> `...`
