```{module} Tools.RenumberByConnection()
:synopsis: Renumber by selection
```

(Tools.RenumberByConnection)=

# Tools.RenumberByConnection

## Description

Renumber by selection

## Syntax

```python
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTarget=[])
```

Macro: {ref}`Macro-Tools-RenumberByConnection`

Ribbon: {menuselection}`Tools --> RenumberByConnection`

## Inputs

**`connectRenumberTool`**
: A _CONNECT_RENUMBER_TOOL_ specifying the renumber tool. The default value is CONNECT_RENUMBER_TOOL().

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTarget=[])
```
