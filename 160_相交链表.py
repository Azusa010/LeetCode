from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B = headA,headB
        while A!= B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# 构建相交链表
common = build_linked_list([8,4,5])
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

sol = Solution()
print(sol.getIntersectionNode(headA,headB).val)