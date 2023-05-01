class Solution:
    def average(self, salary: List[int]) -> float:
        x=sum(salary)-min(salary)-max(salary)
        #print(x)
        return x/(len(salary)-2)