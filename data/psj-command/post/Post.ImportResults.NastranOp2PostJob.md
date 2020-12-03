```{module} Post.ImportResults.NastranOp2PostJob()
:synopsis: import Nastran op2 post job
```

(Post.ImportResults.NastranOp2PostJob)=

# Post.ImportResults.NastranOp2PostJob

## Description

import Nastran op2 post job

## Syntax

```python
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```

Macro: {ref}`Macro-Post-NastranOp2PostJob`

Ribbon: {menuselection}`Post --> ImportResults --> NastranOp2PostJob`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strlPaths`**
: A _String List_ specifying the paths. This is a required input.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```
