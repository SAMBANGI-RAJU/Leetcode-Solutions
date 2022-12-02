# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0 
        s=head
        while s:
            cnt+=1 
            s=s.next
        if cnt==1:
            return head
        mid=cnt//2 
        cnt=0
        while head:
            cnt+=1 
            if cnt==mid:
                return head.next
            head=head.next
            