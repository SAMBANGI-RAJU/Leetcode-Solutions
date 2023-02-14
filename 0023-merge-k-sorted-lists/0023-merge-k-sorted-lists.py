# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=lists 
        arr=[]
        for cur in lists:
            while cur:
                arr.append(cur.val)
                cur=cur.next 
        arr.sort()
        #print(arr)
        dummy=ListNode(0)
        cur=dummy 
        for i in arr:
            cur.next=ListNode(i)
            cur=cur.next 
        return dummy.next