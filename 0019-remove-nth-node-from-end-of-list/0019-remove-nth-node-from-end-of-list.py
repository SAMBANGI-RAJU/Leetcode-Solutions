# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=[]
        s=head
        while s:
            l.append(s.val)
            s=s.next
        
        del l[-n]
        #print(l)
        res=ListNode(0)
        cur=res
        for i in l:
            cur.next=ListNode(i)
            cur=cur.next 
        return res.next
        