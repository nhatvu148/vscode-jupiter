```{module} MeshCleanup.ChangeTopology.Element.SurfaceElement()
:synopsis: Unknown Description
```

(MeshCleanup.ChangeTopology.Element.SurfaceElement)=

# MeshCleanup.ChangeTopology.Element.SurfaceElement

## Description

Unknown Description

## Syntax

```python
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```

Macro: {ref}`Macro-MeshCleanup-ChangeTopologyElement`

Ribbon: {menuselection}`MeshCleanup --> ChangeTopology --> Element --> SurfaceElement`

## Inputs

**`ilElement`**
: A _Integer List_ specifying the element. This is a required input.

**`ilFace`**
: A _Integer List_ specifying the face. This is a required input.

**`ilPart`**
: A _Integer List_ specifying the part. This is a required input.

**`iCreateNewPart`**
: An _Integer_ specifying the create new part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```
