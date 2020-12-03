```{module} Tools.Measure.Mass.Material()
:synopsis: measure mass by material
```

(Tools.Measure.Mass.Material)=

# Tools.Measure.Mass.Material

## Description

measure mass by material

## Syntax

```python
Tools.Measure.Mass.Material(crlPart, crlCondition, strDensity, strTarget="Mass", bGravityCenter=False, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureMassByMaterial`

Ribbon: {menuselection}`Tools --> Measure --> Mass --> Material`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlCondition`**
: A _Cursor List_ specifying the condition. This is a required input.

**`strDensity`**
: A _String_ specifying the density. This is a required input.

**`strTarget`**
: A _String_ specifying the target. The default value is "Mass".

**`bGravityCenter`**
: A _Boolean_ specifying the gravity center. The default value is False.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Mass.Material(crlPart, crlCondition, strDensity, strTarget="Mass", bGravityCenter=False, iPrecision=6)
```
