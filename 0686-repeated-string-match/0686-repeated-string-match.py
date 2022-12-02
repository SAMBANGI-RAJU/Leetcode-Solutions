class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        check = ""
        count = 0
        3#n = len(b)
        
        while len(check) <= 1e4:
            if b in check:
                return count
            else:
                check += a
                count += 1
        
        return -1