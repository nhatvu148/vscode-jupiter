# DeleteSubAssemblyRecursively

## Description

Delete an indicated sub assembly and all the items inside the sub assembly safely.

## Syntax

JPT.DeleteSubAssemblyRecursively(DItem subAssembly)

## Inputs

1. DItem

Target sub assembly.

## Return Code

_Python Output_

- No return value

## Sample Code

_Input:_

```python
SubAsm=JPT.FindSubAssemblyByID(1)
JPT.JPT.DeleteSubAssemblyRecursively(SubAsm)
```

_Output:_
