```{module} MeshCleanup.Element.SurfaceElement()
:synopsis: Change Topology Element
```

(MeshCleanup.Element.SurfaceElement)=

# MeshCleanup.Element.SurfaceElement

## Description

Change Topology Element

## Syntax

```python
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```

Macro: {ref}`Macro-MeshCleanup-ChangeTopologyElement`

Ribbon: {menuselection}`MeshCleanup --> Element --> SurfaceElement`

## Inputs

**`ilElement`**
: A _Integer List_ specifying the element. The default value is [].

**`ilFace`**
: A _Integer List_ specifying the face. The default value is [].

**`ilPart`**
: A _Integer List_ specifying the part. The default value is [].

**`iCreateNewPart`**
: An _Integer_ specifying the create new part. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```
