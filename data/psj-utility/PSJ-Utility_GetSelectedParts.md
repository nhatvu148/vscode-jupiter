# GetSelectedParts

## Description

Get selected part information

## Syntax

GetSelectedParts()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- BodyVector

Selected part information (typeID, id, key, name)

## Sample Code

_Input:_

```python
part = JPT.GetSelectedParts()
for p in part:
    print('type="{0}", id="{1}", key="{2}", name="{3}"'.format(p.typeID, p.id, p.key, p.name))
```

_Output:_

\> `type="3", id="1", key="1", name="Cube_1"`

\> `type="3", id="2", key="2", name="Cube_2"`
