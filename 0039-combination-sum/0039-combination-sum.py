class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def combsum(ind,arr,ds,a,n,target):
            if ind==n:
                if target==0:
                    ds.append(a[:])
                return 
            if arr[ind]<=target:
                a.append(arr[ind])
                combsum(ind,arr,ds,a,n,target-arr[ind])
                a.pop(-1)
            combsum(ind+1,arr,ds,a,n,target)
        ds=[]
        combsum(0,arr,ds,[],len(arr),target)
        return ds
                
        