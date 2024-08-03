from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tar = sorted(target)
        array = sorted(arr)
        if tar == array:
            return True
        return False