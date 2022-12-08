# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def traverse(temp, arr):
            if temp:    
                traverse(temp.left, arr)
                if not temp.left and not temp.right:
                    arr.append(temp.val)
                traverse(temp.right, arr)
        traverse(root1, arr1)
        traverse(root2, arr2)
        return arr1 == arr2