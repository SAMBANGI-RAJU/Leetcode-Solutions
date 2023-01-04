class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d={}
        for i in range(len(tasks)):
            if tasks[i] not in d:
                d[tasks[i]]=1
            else:
                d[tasks[i]]+=1
        #print(d)
        ans=0
        for k,v in d.items():
            if v==1:
                return -1 
            ans += v // 3 + (v % 3 != 0)
        return ans