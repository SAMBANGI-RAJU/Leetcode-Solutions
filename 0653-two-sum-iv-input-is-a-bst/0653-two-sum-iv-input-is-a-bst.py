# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s=set()
        def count(root,s):
            if not root:
                return False
            res = k - root.val 
            if res in s:
                return True 
            s.add(root.val)
            return count(root.left,s) or count(root.right,s)
        return count(root,s)
    