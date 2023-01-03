# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head 
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next 
        arr.reverse()
        dummy=ListNode(0)
        cur=dummy 
        for i in arr:
            cur.next=ListNode(i)
            cur=cur.next 
        return dummy.next 