# ConvertFromDocUnit

## Description

Converts units in the document to SI\[m\] units (Jupiter macro units). The return value will be the value after conversion.

## Syntax

`ConvertFromDocUnit(float inputValue, enum UnitType)`

## Inputs

1. Float

Conversion source value

2. Enum

Unit system conversion type

## Return Code

_Python Output_

- float

Converted Value

## Sample Code

_Input:_

```python
convFromDoc = JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)
print(str(convFromDoc))
```

_Output:_

\> `0.001`
