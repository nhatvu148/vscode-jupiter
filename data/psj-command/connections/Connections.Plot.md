```{module} Connections.Plot()
:synopsis: Create 1D plot connection
```

(Connections.Plot)=

# Connections.Plot

## Description

Create 1D plot connection

## Syntax

```python
Connections.Plot(strName="PLOT_1", iPID=1, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Connections-Property1DPlot`

Ribbon: {menuselection}`Connections --> Plot`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PLOT_1".

**`iPID`**
: An _Integer_ specifying the p ID. The default value is 1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Plot(strName="PLOT_1", iPID=1, crlTarget=[], crEdit=None)
```
