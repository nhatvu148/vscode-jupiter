```{module} Assembly.RightClick.Suppress()
:synopsis: Suppress/ Unsuppress part on Tree Assembly
```

(Assembly.RightClick.Suppress)=

# Assembly.RightClick.Suppress

## Description

Suppress/ Unsuppress part on Tree Assembly

## Syntax

```python
Assembly.RightClick.Suppress(crlPart=[])
```

Macro: {ref}`Macro-Assembly-Suppress`

Ribbon: {menuselection}`Assembly --> RightClick --> Suppress`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.Suppress(crlPart=[])
```
