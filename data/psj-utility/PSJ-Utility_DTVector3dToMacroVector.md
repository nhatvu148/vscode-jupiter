# DTVector3dToMacroVector

## Description

Convert Vector3d object to vector3d macro string

## Inputs

1. Vector3d object (DTVector3d class)

## Return Code

vector3d macro string (string)

## Sample Code

```python
listDNodeObject = JPT.GetAllNodes()
posNode1 = listDNodeObject[0].pos
JPT.DTVector3dToMacroVector(posNode1)
```
