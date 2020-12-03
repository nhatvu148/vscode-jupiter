```{module} Properties.ElemRelatedInfo.Conn()
:synopsis: Set Shell Parameter
```

(Properties.ElemRelatedInfo.Conn)=

# Properties.ElemRelatedInfo.Conn

## Description

Set Shell Parameter

## Syntax

```python
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```

Macro: {ref}`Macro-Properties-ElemRelatedInfo_Conn`

Ribbon: {menuselection}`Properties --> ElemRelatedInfo --> Conn`

## Inputs

**`listEricontEndProp`**
: A _ERICONT_END_PROP List_ specifying the ericont end property. The default value is [].

**`listEricontOriVecProp`**
: A _ERICONT_ORI_VEC_PROP List_ specifying the ericont ori vector property. The default value is [].

**`listCidProp`**
: A _CID_PROP List_ specifying the cid property. The default value is [].

**`listEricontDamperLocProp`**
: A _ERICONT_DAMPER_LOC_PROP List_ specifying the ericont damper location property. The default value is [].

**`listOcidProp`**
: A _OCID_PROP List_ specifying the ocid property. The default value is [].

**`listDamperOffsetVecs`**
: A _DAMPER_OFFSET_VECS List_ specifying the damper offset vecs. The default value is [].

**`listEricontNodeidProp`**
: A _ERICONT_NODEID_PROP List_ specifying the ericont nodeid property. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```
