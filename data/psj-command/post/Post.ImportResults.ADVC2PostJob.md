```{module} Post.ImportResults.ADVC2PostJob()
:synopsis: Post ImportResults ADVC2PostJob
```

(Post.ImportResults.ADVC2PostJob)=

# Post.ImportResults.ADVC2PostJob

## Description

Post ImportResults ADVC2PostJob

## Syntax

```python
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```

Macro: {ref}`Macro-Post-ADVC2PostJob`

Ribbon: {menuselection}`Post --> ImportResults --> ADVC2PostJob`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strlResultFolderPaths`**
: A _String List_ specifying the result folder paths. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```
