```{module} Connections.Contacts.NXNastran.ContactTable()
:synopsis: Create Contact NXNastran Contact Table
```

(Connections.Contacts.NXNastran.ContactTable)=

# Connections.Contacts.NXNastran.ContactTable

## Description

Create Contact NXNastran Contact Table

## Syntax

```python
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```

Macro: {ref}`Macro-Connections-LbcContactTableNXNastran`

Ribbon: {menuselection}`Connections --> Contacts --> NXNastran --> ContactTable`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iAlg`**
: An _Integer_ specifying the algorithm. The default value is 0.

**`dNorPenFactor`**
: A _Double_ specifying the nor pen factor. The default value is 0.

**`dTanPenFactor`**
: A _Double_ specifying the tan pen factor. The default value is 0.

**`dForceConTol`**
: A _Double_ specifying the force con tolerance. The default value is 0.

**`dMaxForceIter`**
: A _Double_ specifying the maximum force iterator. The default value is 0.

**`dMaxStaIter`**
: A _Double_ specifying the maximum sta iterator. The default value is 0.

**`dChangeNum`**
: A _Double_ specifying the change number. The default value is 0.

**`dMinContactPer`**
: A _Double_ specifying the minimum contact per. The default value is 0.

**`iShellThickness`**
: An _Integer_ specifying the shell thickness. The default value is 0.

**`iContactStatus`**
: An _Integer_ specifying the contact status. The default value is 0.

**`iInitGapPenetra`**
: An _Integer_ specifying the initial gap penetra. The default value is 0.

**`iRegionRefine`**
: An _Integer_ specifying the region refine. The default value is 0.

**`iEvaluPts`**
: An _Integer_ specifying the evalu pts. The default value is 0.

**`dMinSearDist`**
: A _Double_ specifying the minimum sear dist. The default value is 0.

**`dMaxSearDist`**
: A _Double_ specifying the maximum sear dist. The default value is 0.

**`dFricCoef`**
: A _Double_ specifying the fric coefficient . The default value is 0.

**`dSearchDist`**
: A _Double_ specifying the search dist. The default value is 0.

**`dPenatlyFactor`**
: A _Double_ specifying the penatly factor. The default value is 0.

**`iShellOffset`**
: An _Integer_ specifying the shell offset. The default value is 0.

**`crplTargetPair`**
: A _Cursor Pair List_ specifying the target pair. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```
