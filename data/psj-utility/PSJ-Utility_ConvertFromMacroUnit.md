# ConvertFromMacroUnit

## Description

Convert unit system from user input unit to macro SI unit

## Syntax

ConvertFromMacroUnit(float inputValue, enum UnitType, string strUnit)

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
convFromMacr = JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit_Length, 'mm')
print(str(convFromMacr))
```

_Output:_

\> `0.001`
