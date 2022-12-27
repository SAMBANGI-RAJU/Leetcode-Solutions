class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf
        self.dfs(root)
        return self.max_sum

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = max(0, self.dfs(node.left)) # calculate the maximum path sum of any path in the left subtree which begins in the current node
        right = max(0, self.dfs(node.right)) # calculate the maximum path sum of any path in the right subtree which begins in the current node
        self.max_sum = max(self.max_sum, left + node.val + right) # choose a path with the maximal path sum in the overall tree
        return node.val + max(left, right) # return the maximum path sum of any path which begins in the current node