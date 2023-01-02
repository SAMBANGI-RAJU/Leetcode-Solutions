# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur=list1
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next 
        cur2=list2
        while cur2:
            res.append(cur2.val)
            cur2=cur2.next
        res.sort()
        f_list=ListNode(0)
        cur2=f_list
        for i in res:
            cur2.next=ListNode(i)
            cur2=cur2.next
        return f_list.next
        