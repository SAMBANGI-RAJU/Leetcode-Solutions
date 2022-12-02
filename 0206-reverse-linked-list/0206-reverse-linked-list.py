# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        s=head 
        while head:
            arr.append(head.val)
            head=head.next 
        head=s
        for i in arr[::-1]:
            s.val=i 
            s=s.next 
        return head