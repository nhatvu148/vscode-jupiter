```{module} Connections.Contacts.ExportCheckReport()
:synopsis: Unknown Description
```

(Connections.Contacts.ExportCheckReport)=

# Connections.Contacts.ExportCheckReport

## Description

Unknown Description

## Syntax

```python
Connections.Contacts.ExportCheckReport(strFullPath, dZoomFactor=1.2, iFitBy=0, iListBy=0, iListOrder=0, iFormat=0)
```

Macro: {ref}`Macro-Connections-CreateContactReport`

Ribbon: {menuselection}`Connections --> Contacts --> ExportCheckReport`

## Inputs

**`strFullPath`**
: A _String_ specifying the full path. This is a required input.

**`dZoomFactor`**
: A _Double_ specifying the zoom factor. The default value is 1.2.

**`iFitBy`**
: An _Integer_ specifying the fit by. The default value is 0.

**`iListBy`**
: An _Integer_ specifying the list by. The default value is 0.

**`iListOrder`**
: An _Integer_ specifying the list order. The default value is 0.

**`iFormat`**
: An _Integer_ specifying the format. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.ExportCheckReport(strFullPath, dZoomFactor=1.2, iFitBy=0, iListBy=0, iListOrder=0, iFormat=0)
```
