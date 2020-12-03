# ConvertValueToDocUnit

## Description

Convert value from SI unit system to JPT user setup unit

## Syntax

ConvertValueToDocUnit(float inputValue, enum UnitTypeunit)

## Inputs

1. Float

Conversion source value

2. Enum

Unit system conversion type

## Return Code

_Python Output_

- float

Converted value

## Sample Code

_Input:_

```python
convToDoc = JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)
print(str(convToDoc))
```

_Output:_

\> `1000.0`
