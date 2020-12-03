# Exec

## Description

Run Jupiter macro

## Syntax

Exec(string macroCommand)

## Inputs

1. string

Macro command

## Return Code

_Python Output_

- Refer each macro command

## Sample Code

_Input:_

```python
res = JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0) ')
print(res)
```

_Output:_

\> `1`
