```{module} MeshEdit.SeparateNodes()
:synopsis: Separate nodes
```

(MeshEdit.SeparateNodes)=

# MeshEdit.SeparateNodes

## Description

Separate nodes

## Syntax

```python
MeshEdit.SeparateNodes(crlShareNodes=[], crlTarget=[], iKeepNodeIDsOn=0)
```

Macro: {ref}`Macro-MeshEdit-SeparateNode`

Ribbon: {menuselection}`MeshEdit --> SeparateNodes`

## Inputs

**`crlShareNodes`**
: A _Cursor List_ specifying the share nodes. The default value is [].

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iKeepNodeIDsOn`**
: An _Integer_ specifying the keep node i ds on. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.SeparateNodes(crlShareNodes=[], crlTarget=[], iKeepNodeIDsOn=0)
```
