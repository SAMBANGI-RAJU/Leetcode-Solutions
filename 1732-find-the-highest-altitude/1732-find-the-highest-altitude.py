class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        sum=0 
        for i in gain:
            sum+=i 
            res.append(sum)
        #print(res)
        return max(res)