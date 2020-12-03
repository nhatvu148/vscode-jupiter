# MacroResultToListString

## Description

Parse returned string from macro to list of string

## Inputs

1. returned string from macro (string)

## Return Code

list of string (list)

## Sample Code

```python
result = JPT.Exec('MC_Mesh_Quality_Manual_Check_Tri([3:1], 0, 0, 0.1)')
listString = JPT.MacroResultToListString(result)
```
