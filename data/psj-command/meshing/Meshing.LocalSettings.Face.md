```{module} Meshing.LocalSettings.Face()
:synopsis: LocalSettings.Face
```

(Meshing.LocalSettings.Face)=

# Meshing.LocalSettings.Face

## Description

LocalSettings.Face

## Syntax

```python
Meshing.LocalSettings.Face(strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None)
```

Macro: {ref}`Macro-Meshing-CreateLocalSetting_Face`

Ribbon: {menuselection}`Meshing --> LocalSettings --> Face`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`localMesh`**
: A _LOCAL_MESH_ specifying the mesh. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`ilHardPointId`**
: A _Integer List_ specifying the hard point ID. The default value is [].

**`veclHardPointXYZ`**
: A _Vector List_ specifying the hard point x y z. The default value is [].

**`crlHardPointTarget`**
: A _Cursor List_ specifying the hard point target. The default value is [].

**`crEditTarget`**
: A _Cursor_ specifying the edit target. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalSettings.Face(strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None)
```
