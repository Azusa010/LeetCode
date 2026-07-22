from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         pre = None
#         cur = head
#         while cur is not None:
#             temp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = temp
#         return pre

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur,pre):
            if not cur:
                return pre
            res = recur(cur.next,cur)
            cur.next = pre
            return res
        return recur(head,None)
        
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
reversed_head = Solution().reverseList(l1)
cur = reversed_head
while cur:
    print(cur.val, end=" ")
    cur = cur.next