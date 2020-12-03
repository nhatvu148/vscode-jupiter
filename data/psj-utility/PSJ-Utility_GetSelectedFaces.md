# GetSelectedFaces

## Description

Get selected face information

## Syntax

GetSelectedFaces()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- FaceVector

Selected face information (typeID, id, key)

## Sample Code

_Input:_

```python
faces = JPT.GetSelectedFaces()
for f in faces:
    print(str(f.id)+' '+str(f.key)+' '+str(f.typeID))
```

_Output:_

\> `22 22 6`

\> `26 26 6`

\> `31 31 6`
