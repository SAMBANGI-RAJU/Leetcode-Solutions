class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,cursum):
            if not root:
                return 
            cursum+=root.val 
            if not root.left and not root.right:
                return cursum==targetSum 
            return helper(root.left,cursum) or helper(root.right,cursum)
        return helper(root,0)