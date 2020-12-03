# FindSubAssemblyByID

## Description

Find SubAssembly by ID

## Syntax

FindSubAssemblyByID(int SubAssemblyID)

## Inputs

1. int

Id of search target sub assembly

## Return Code

_Python Output_

- DItem

Found sub assembly information.

## Sample Code

_Input:_

```python
SubAsm=JPT.FindSubAssemblyByID(1)
print(SubAsm.name)
```

_Output:_

\> `SubAsmName`
