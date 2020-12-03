# GetJTDBVersion

## Description

Get version of documents

## Syntax

GetJTDBVersion()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- vector VersionInfo

Version values of document (build, major, minor, sub)

## Sample Code

_Input:_

```python
ver=JPT.GetJTDBVersion()
print(str(ver.build)+' '+str(ver.major)+' '+str(ver.minor)+' '+str(ver.sub))
```

_Output:_

\> `55 0 0 1`
