class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        def binarysearch(spell):
            (l,r) = (0,len(potions)-1)
            while l<=r:
                mid = (l+r)//2
                prod = spell*potions[mid]
                if prod>=success:
                    r = mid-1
                else:
                    l = mid+1
            return l
        for spell in spells:
            idx = binarysearch(spell)
            res.append(len(potions)-idx)
        return res
        