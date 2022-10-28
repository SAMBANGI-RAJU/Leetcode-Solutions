class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        
        R = len(A)
        C = len(A[0])
        
        la = []
        lb = []
        
        v = collections.Counter()
        
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    la.append((r, c))
                if B[r][c] == 1:
                    lb.append((r, c))
        
        for ax, ay in la:
            for bx, by in lb:
                k = (ax-bx, ay-by)
                v[k] += 1
        
        
        
        return max(v.values() or [0])