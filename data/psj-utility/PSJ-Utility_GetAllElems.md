# GetAllElems

## Description

Get information of elements

## Syntax

GetAllElems()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- ElemVector

Element information (id, key, type, typeID)

## Sample Code

_Input:_

```python
elem= JPT.GetAllElems()
for e in elem:
    print(str(e.typeID)+' '+str(e.type)+' '+str(e.id)+' '+str(e.key))
```

_Output:_

\> `11 ELEMTYPE_TRI3 772 772`

\> `11 ELEMTYPE_TRI3 1878 1878`

\> `11 ELEMTYPE_TRI3 251 251`

\> `...`
