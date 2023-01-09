# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_inorder(self, root):
        if not root:
            return []
        else:
            return self.dfs_inorder(root.left) + [root.val] + self.dfs_inorder(root.right)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree_elements = self.dfs_inorder(root)
        for i in range(1, len(tree_elements)):
            if tree_elements[i] <= tree_elements[i - 1]:
                return False
        return True