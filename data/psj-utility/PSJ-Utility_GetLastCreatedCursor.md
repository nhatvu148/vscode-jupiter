# GetLastCreatedCursor

## Description

Get the latest id of created entity

## Syntax

GetLastCreatedCursor()

## Inputs

1. NONE

No input value

## Return Code

_Python Output_

- DItemVector

Last created Object

## Sample Code

_Input:_

```python
for i in JPT.GetLastCreatedCursor():
    print('{0}, {1}'.format(i.type, i.id))
```

_Output:_

\> `BODY, 2`
\> `EDGE, 27`
\> `EDGE, 28`
\> `FACE, 29`
\> `FACE, 30`
\> `FACE, 31`
\> `BODYLINK, 27`
\> `BODYLINK, 28`
\> `BODYLINK, 29`
\> `BODYLINK, 30`
\> `BODYLINK, 31`
\> `SHAPELINK, 49`
\> `SHAPELINK, 50`
\> `SHAPELINK, 51`
\> `SHAPELINK, 52`
\> `NODE, 489`
\> `NODE, 490`
\> `...`
