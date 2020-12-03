```{module} MeshCleanup.Manual2D.SplitElement.QuadToQuadTri()
:synopsis: Unknown Description
```

(MeshCleanup.Manual2D.SplitElement.QuadToQuadTri)=

# MeshCleanup.Manual2D.SplitElement.QuadToQuadTri

## Description

Unknown Description

## Syntax

```python
MeshCleanup.Manual2D.SplitElement.QuadToQuadTri(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```

Macro: {ref}`Macro-MeshCleanup-SplitElement`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> SplitElement --> QuadToQuadTri`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

**`crDatumNode0`**
: A _Cursor_ specifying the datum node0. The default value is None.

**`crDatumNode1`**
: A _Cursor_ specifying the datum node1. The default value is None.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iAutoExecute`**
: An _Integer_ specifying the auto execute. The default value is 0.

**`iAutoTransition`**
: An _Integer_ specifying the auto transition. The default value is 0.

**`iCADProject`**
: An _Integer_ specifying the CAD project. The default value is 0.

**`iMergeNode`**
: An _Integer_ specifying the merge node. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.SplitElement.QuadToQuadTri(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```
