# GetSelectedElems

## Description

Get selected element information

## Syntax

GetSelectedElems()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- ElemVector

Selected element information (typeID, type, id, key, kind)

## Sample Code

_Input:_

```python
elems = JPT.GetSelectedElems()
for e in elems:
    print(str(e.typeID)+' '+str(e.type)+' '+str(e.id)+' '+str(e.key)+' '+str(e.kind))
```

_Output:_

\> `11 ELEMTYPE_TRI3 1161 1161 ELEMKIND_2D`

\> `11 ELEMTYPE_TRI3 1171 1171 ELEMKIND_2D`

\> `11 ELEMTYPE_TRI3 1173 1173 ELEMKIND_2D`
