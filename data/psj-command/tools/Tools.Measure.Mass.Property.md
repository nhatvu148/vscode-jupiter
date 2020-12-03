```{module} Tools.Measure.Mass.Property()
:synopsis: measure mass using applied property
```

(Tools.Measure.Mass.Property)=

# Tools.Measure.Mass.Property

## Description

measure mass using applied property

## Syntax

```python
Tools.Measure.Mass.Property(crlPart, crlCondition, strTarget="Mass", bGravityCenter=False, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureMassByProperty`

Ribbon: {menuselection}`Tools --> Measure --> Mass --> Property`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlCondition`**
: A _Cursor List_ specifying the condition. This is a required input.

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
Tools.Measure.Mass.Property(crlPart, crlCondition, strTarget="Mass", bGravityCenter=False, iPrecision=6)
```
