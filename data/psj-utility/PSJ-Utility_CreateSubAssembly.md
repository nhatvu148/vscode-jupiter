# CreateSubAssembly

## Description

Create a new sub assembly under the indicated parent sub assembly.

## Syntax

CreateSubAssembly(string name, DItemW parent)

## Inputs

1. string

create sub assembly name

2. DItemW

parent assembly tree item

## Return Code

_Python Output_

- DItemW

Create Tree Item

## Sample Code

_Input:_

```python
JPT.CreateSubAssembly('CreateSubAsm',JPT.DItem())
SubAsm=JPT.GetSubAssemblyById(1)
JPT.CreateSubAssembly('AddSubAsm',SubAsm)
```

_Output:_

![](./../_images/CreateSubAsm.png)
