```{module} Tools.RenumberByFile()
:synopsis: Renumber By File
```

(Tools.RenumberByFile)=

# Tools.RenumberByFile

## Description

Renumber By File

## Syntax

```python
Tools.RenumberByFile(strCSVPath="", iConfilctStrategy=0, bNeedToUpdateCount=False)
```

Macro: {ref}`Macro-Tools-RenumberByFile`

Ribbon: {menuselection}`Tools --> RenumberByFile`

## Inputs

**`strCSVPath`**
: A _String_ specifying the CSV path. The default value is "".

**`iConfilctStrategy`**
: An _Integer_ specifying the confilct strategy. The default value is 0.

**`bNeedToUpdateCount`**
: A _Boolean_ specifying the need to update count. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.RenumberByFile(strCSVPath="", iConfilctStrategy=0, bNeedToUpdateCount=False)
```
