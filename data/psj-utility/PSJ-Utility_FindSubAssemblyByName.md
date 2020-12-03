# FindSubAssemblyByName

## Description

Find SubAssembly by Name

## Syntax

FindSubAssemblyByName(string SubAssemblyName)

## Inputs

1. String

Name of search target sub assembly

## Return Code

_Python Output_

- DItemVector

Found sub assemblies.

## Sample Code

_Input:_

```python
SubAsm=JPT.FindSubAssemblyByName('MySubAsms')
for i in SubAsm
    print(i.name)
```

_Output:_

\> `MySubAsms`
