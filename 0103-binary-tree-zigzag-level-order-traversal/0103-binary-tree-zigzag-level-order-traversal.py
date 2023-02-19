# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        lorder=defaultdict(list   )
        def dfs(node,level):
            lorder[level].append(node.val)
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        dfs(root,0)
        #print(lorder)
        ans=[]
        flag=True
        for i in lorder.values():
            if flag==True:
                ans.append(i)
                flag=False
            else:
                ans.append(i[::-1])
                flag=True
        return ans
            
            
        