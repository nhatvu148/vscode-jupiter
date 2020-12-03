```{module} Post.ImportResults.NastranHDF5()
:synopsis: Import Nastran HDF5PostJob file
```

(Post.ImportResults.NastranHDF5)=

# Post.ImportResults.NastranHDF5

## Description

Import Nastran HDF5PostJob file

## Syntax

```python
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```

Macro: {ref}`Macro-Post-NastranHDF5PostJob`

Ribbon: {menuselection}`Post --> ImportResults --> NastranHDF5`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`strlPaths`**
: A _String List_ specifying the paths. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```
