# GetOpnList

## Description

Get list of Launch Operation

## Syntax

GetOpnList()

## Inputs

1. NONE

No input value

## Return Code

_Python Output_

- String

List of Launch Operation

## Sample Code

_Input:_

```python
get = JPT.GetOpnList()
for s in get:
    print(s)
```

_Output:_

\> `MESH_EDIT_GEOM_EDIT_FCIRC_VERTEX_ADJUST`

\> `MMC_MUFFLER_MANUAL_PIPE_MERGE_FACES_CIRCUMFERENTIAL`

\> `ENG_NVH_AUTO_BUSH`

\> `THICKNESS_DISTRIBUTION`

\> `....`
