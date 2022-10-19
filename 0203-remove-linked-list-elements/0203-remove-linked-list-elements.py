# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=head 
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next
        while val in res:
            res.remove(val)
        #print(res)
        f=ListNode(0)
        cur=f 
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return f.next
            