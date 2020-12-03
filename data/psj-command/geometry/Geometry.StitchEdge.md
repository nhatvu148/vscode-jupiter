```{module} Geometry.StitchEdge()
:synopsis: Stitch Edges
```

(Geometry.StitchEdge)=

# Geometry.StitchEdge

## Description

Stitch Edges

## Syntax

```python
Geometry.StitchEdge(dTolerance=0.3, bKeepSlave=True, crlMaster=[], crlSlave=[])
```

Macro: {ref}`Macro-Geometry-StitchEdge`

Ribbon: {menuselection}`Geometry --> StitchEdge`

## Inputs

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.3.

**`bKeepSlave`**
: A _Boolean_ specifying the keep slave. The default value is True.

**`crlMaster`**
: A _Cursor List_ specifying the master. The default value is [].

**`crlSlave`**
: A _Cursor List_ specifying the slave. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.StitchEdge(dTolerance=0.3, bKeepSlave=True, crlMaster=[], crlSlave=[])
```
