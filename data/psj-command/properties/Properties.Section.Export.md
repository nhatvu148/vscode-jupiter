```{module} Properties.Section.Export()
:synopsis: export 1D section to xml file
```

(Properties.Section.Export)=

# Properties.Section.Export

## Description

export 1D section to xml file

## Syntax

```python
Properties.Section.Export(strExportSavePath="")
```

Macro: {ref}`Macro-Properties-Property1DSectionExport`

Ribbon: {menuselection}`Properties --> Section --> Export`

## Inputs

**`strExportSavePath`**
: A _String_ specifying the export save path. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Section.Export(strExportSavePath="")
```
