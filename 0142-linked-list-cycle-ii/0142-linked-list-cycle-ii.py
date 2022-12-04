# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, curr = head, head, head
        
        # Get to the point where slow and fast meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        # Check if we reached the end without slow and fast meeting, if so, there is no cycle
        if not fast or not fast.next:
            return None
        
        # Othewise, we're at the meeting point. Now let's move curr and slow onwards until they both meet
        while curr != slow:
            curr = curr.next
            slow = slow.next
        
        # Now they've met, and this is also the point of the cycle
        return curr