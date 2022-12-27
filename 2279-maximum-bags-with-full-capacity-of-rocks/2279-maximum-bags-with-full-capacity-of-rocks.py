class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffBag = []
        # determine the difference betwin max capacity and current rocks
        for c, r in zip(capacity,rocks):
            diffBag.append(c-r)
        
        diffBag.sort()
        
        filledbags = 0
        #count bags that can be filed
        for f in diffBag:
            if f == 0:
                filledbags += 1
                continue
            
            if additionalRocks <= 0:
                return filledbags
            
            if f <= additionalRocks:
                filledbags += 1
            additionalRocks -= f
        
        return filledbags
                
                
        