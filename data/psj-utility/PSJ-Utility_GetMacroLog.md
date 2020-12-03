# GetMacroLog

## Description

Get all of the macro in Macro Window

## Syntax

GetMacroLog()

## Inputs

1. NONE

No input value

## Return Code

_Python Output_

- String

List of previous Macro in Macro Window

## Sample Code

_Input:_

```python
print(JPT.GetMacroLog())
```

_Output:_

\> `LaunchOperation("GEOMETRY_CREATE_ENTITY_PARTS_CUBE", 0)`
\> `CreateCube(\[0, 0, 0\], \[0.01, 0.01, 0.01\], \[10, 10, 10\], "Cube_1", 7105764, 0:0)`
\> `LaunchOperation("GEOMETRY_CREATE_ENTITY_PARTS_CYLINDER", 0)`
\> `CreateCylinderFrustum(\[0, 0, 0\], 0.01, 0.01, 0.01, 36, 10, "Cylinder_1", 6409934, 0:0)`
