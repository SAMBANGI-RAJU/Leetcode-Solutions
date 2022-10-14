# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        cur=head 
        while cur:
            res.append(cur.val)
            cur=cur.next 
        #print(res)
        n=len(res)
        mid=n//2 
        #print(res[mid])
        res_list=ListNode(0)
        dummy=res_list 
        for i in range(len(res)):
            if i!=mid:
                dummy.next=ListNode(res[i])
                dummy=dummy.next 
        return res_list.next
        