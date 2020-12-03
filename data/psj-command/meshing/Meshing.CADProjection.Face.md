```{module} Meshing.CADProjection.Face()
:synopsis: CadProject for Face
```

(Meshing.CADProjection.Face)=

# Meshing.CADProjection.Face

## Description

CadProject for Face

## Syntax

```python
Meshing.CADProjection.Face(iMethod=2, crCadPart=None, crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```

Macro: {ref}`Macro-Meshing-CadProject_Face`

Ribbon: {menuselection}`Meshing --> CADProjection --> Face`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 2.

**`crCadPart`**
: A _Cursor_ specifying the CAD part. The default value is None.

**`crlMeshedFace`**
: A _Cursor List_ specifying the meshed face. The default value is [].

**`bForceProject`**
: A _Boolean_ specifying the force project. The default value is False.

**`bProjectCornerNodes`**
: A _Boolean_ specifying the project corner nodes. The default value is True.

**`bProjectMidNodes`**
: A _Boolean_ specifying the project mid nodes. The default value is False.

**`bIDcheck`**
: A _Boolean_ specifying the ID check. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.CADProjection.Face(iMethod=2, crCadPart=None, crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```
