class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        edges = collections.defaultdict(list)
        for i in range(len(parent)):
            edges[parent[i]].append(i)

        res = 1

        def dfs(num,edges):
            nonlocal res
            largestSum = secLargest = 0
            if len(edges[num])==0:
                return 1
            for i in edges[num]:
                summ = dfs(i,edges)
                if s[num]!=s[i]:
                    if summ>largestSum:
                        secLargest,largestSum = largestSum,summ
                    elif secLargest<summ:
                        secLargest = summ
            res = max(res,secLargest+largestSum+1)
            return largestSum+1
        dfs(0,edges)
        return res 
        