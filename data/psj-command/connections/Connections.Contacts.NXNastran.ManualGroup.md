```{module} Connections.Contacts.NXNastran.ManualGroup()
:synopsis: Create Contact NXNastran Manual Group
```

(Connections.Contacts.NXNastran.ManualGroup)=

# Connections.Contacts.NXNastran.ManualGroup

## Description

Create Contact NXNastran Manual Group

## Syntax

```python
Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None)
```

Macro: {ref}`Macro-Connections-LbcContactManualGroupNXNastran`

Ribbon: {menuselection}`Connections --> Contacts --> NXNastran --> ManualGroup`

## Inputs

**`crFaceMaster`**
: A _Cursor_ specifying the face master. The default value is None.

**`crFaceSlave`**
: A _Cursor_ specifying the face slave. The default value is None.

**`strName`**
: A _String_ specifying the name. The default value is "ContactNXNastran_1".

**`iContactType`**
: An _Integer_ specifying the contact type. The default value is 0.

**`iContactAlg`**
: An _Integer_ specifying the contact algorithm. The default value is 0.

**`dNorPenFactor`**
: A _Double_ specifying the nor pen factor. The default value is 10.

**`dTanPenFactor`**
: A _Double_ specifying the tan pen factor. The default value is 1.

**`dForceConTol`**
: A _Double_ specifying the force con tolerance. The default value is 0.01.

**`dMaxForceIter`**
: A _Double_ specifying the maximum force iterator. The default value is 10.

**`dMaxStaIter`**
: A _Double_ specifying the maximum sta iterator. The default value is 20.

**`dChangeNum`**
: A _Double_ specifying the change number. The default value is 0.02.

**`dMinContactPer`**
: A _Double_ specifying the minimum contact per. The default value is 100.

**`iShellThickness`**
: An _Integer_ specifying the shell thickness. The default value is 0.

**`iContactStatus`**
: An _Integer_ specifying the contact status. The default value is 0.

**`iInitGapPenetra`**
: An _Integer_ specifying the initial gap penetra. The default value is 0.

**`iRegionRefine`**
: An _Integer_ specifying the region refine. The default value is 0.

**`iEvaluPts`**
: An _Integer_ specifying the evalu pts. The default value is 1.

**`dMinSearDist`**
: A _Double_ specifying the minimum sear dist. The default value is 0.

**`dMaxSearDist`**
: A _Double_ specifying the maximum sear dist. The default value is 0.01.

**`dFricCoef`**
: A _Double_ specifying the fric coefficient . The default value is 0.

**`dSearchDist`**
: A _Double_ specifying the search dist. The default value is 0.

**`dPenatlyFactor`**
: A _Double_ specifying the penatly factor. The default value is 0.

**`iShellOffset`**
: An _Integer_ specifying the shell offset. The default value is 0.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None)
```
