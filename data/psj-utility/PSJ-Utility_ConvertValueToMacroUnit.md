# ConvertValueToMacroUnit

## Description

Convert unit system from macro SI unit to user input unit

## Syntax

ConvertValueToMacroUnit(float inputValue, enum UnitType, string strUnit)

## Inputs

1. Float

Conversion source value

2. Enum

Unit system conversion type

3. String

Unit abbreviation

## Return Code

_Python Output_

- float

Converted value

## Sample Code

_Input:_

```python
convToMacr = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm')
print(str(convToMacr))
```

_Output:_

\> `1000.0`
