```{module} Meshing.CADProjection.FaceToFace()
:synopsis: CadProject for Fact to Face
```

(Meshing.CADProjection.FaceToFace)=

# Meshing.CADProjection.FaceToFace

## Description

CadProject for Fact to Face

## Syntax

```python
Meshing.CADProjection.FaceToFace(iMethod=3, crlCadFace=[], crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```

Macro: {ref}`Macro-Meshing-CadProject_FaceToFace`

Ribbon: {menuselection}`Meshing --> CADProjection --> FaceToFace`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 3.

**`crlCadFace`**
: A _Cursor List_ specifying the CAD face. The default value is [].

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
Meshing.CADProjection.FaceToFace(iMethod=3, crlCadFace=[], crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```
