```{module} MeshEdit.CreateNode.Import()
:synopsis: create node by importing CSV file
```

(MeshEdit.CreateNode.Import)=

# MeshEdit.CreateNode.Import

## Description

create node by importing CSV file

## Syntax

```python
MeshEdit.CreateNode.Import(strCsvFilePath)
```

Macro: {ref}`Macro-MeshEdit-CreateNodeImport`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> Import`

## Inputs

**`strCsvFilePath`**
: A _String_ specifying the csv file path. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.Import(strCsvFilePath)
```
