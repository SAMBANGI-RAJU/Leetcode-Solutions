# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head 
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next 
        #print(res)
        n=len(res)
        mid=n//2
        res.pop(mid)
        dummy=ListNode(0)
        cur=dummy 
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next 
        return dummy.next