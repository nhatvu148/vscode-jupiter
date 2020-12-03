```{module} MainWindow.RightClick.MergeFaces()
:synopsis: Merge Faces
```

(MainWindow.RightClick.MergeFaces)=

# MainWindow.RightClick.MergeFaces

## Description

Merge Faces

## Syntax

```python
MainWindow.RightClick.MergeFaces(crlFace, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```

Macro: {ref}`Macro-MainWindow-bMergeFace`

Ribbon: {menuselection}`MainWindow --> RightClick --> MergeFaces`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`bIsMergeEdge`**
: A _Boolean_ specifying the is merge edge. The default value is False.

**`bRemoveNonBoundEdge`**
: A _Boolean_ specifying the remove non boundary edge. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MainWindow.RightClick.MergeFaces(crlFace, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```
