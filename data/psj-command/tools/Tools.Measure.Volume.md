```{module} Tools.Measure.Volume()
:synopsis: measure volume of parts
```

(Tools.Measure.Volume)=

# Tools.Measure.Volume

## Description

measure volume of parts

## Syntax

```python
Tools.Measure.Volume(crlPart, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureVolumeParts`

Ribbon: {menuselection}`Tools --> Measure --> Volume`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Volume(crlPart, iPrecision=6)
```
