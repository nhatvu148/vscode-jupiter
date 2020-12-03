```{module} Properties.ThicknessDistribution()
:synopsis: Properties view Thickness Distribution
```

(Properties.ThicknessDistribution)=

# Properties.ThicknessDistribution

## Description

Properties view Thickness Distribution

## Syntax

```python
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```

Macro: {ref}`Macro-Properties-ThicknessDistribution`

Ribbon: {menuselection}`Properties --> ThicknessDistribution`

## Inputs

**`dMax`**
: A _Double_ specifying the maximum. The default value is 1.

**`dMin`**
: A _Double_ specifying the minimum. The default value is 0.

**`iByEach`**
: An _Integer_ specifying the by each. The default value is 0.

**`dlThicknessValueSet`**
: A _Double List_ specifying the thickness value set. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```
