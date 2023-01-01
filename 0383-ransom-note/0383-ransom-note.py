class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        return Counter(a)<=Counter(b)