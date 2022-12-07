# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=[]
        def inorder(root):
            if not root:
                return []
            inorder(root.right)
            res.append(root.val)
            inorder(root.left)
        inorder(root)
        lowin=res.index(low)
        higind=res.index(high)
        if higind>lowin:
            return sum(res[lowin:higind+1])
        else:
            return sum(res[higind:lowin+1])