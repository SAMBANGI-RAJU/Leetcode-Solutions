# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])                       #   <-- initialize the queue
        #print(queue[0])
        while queue[0]:                             #   <-- if and while top queue node is not null, pop   
            node = queue.popleft()                  #       it and then push its left child and right  
            queue.extend([node.left, node.right])   #       child onto the queue.

        while queue and not queue[0]:               #   <-- if and while top queue node is null, pop it. 
            queue.popleft()                         #        

        return not queue 