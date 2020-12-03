# GetAllFaces

## Description

Get information of faces

## Syntax

GetAllFaces()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- FaceVector

Face information (id, key, typeID)

## Sample Code

_Input:_

```python
faces = JPT.GetAllFaces()
for f in faces:
    print(str(f.id)+' '+str(f.key)+' '+str(f.typeID))
```

_Output:_

\> `21 21 6`

\> `22 22 6`

\> `23 23 6`

\> `24 24 6`

\> `25 25 6`

\> `...`
