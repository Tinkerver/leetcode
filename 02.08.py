# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not (head and head.next and head.next.next):
            return None
        p, q = head.next, head.next.next
        while q and q.next and p != q:
            p = p.next
            q = q.next.next

        if not (q and q.next):
            return None

        q = head
        while p != q:
            p = p.next
            q = q.next
        return p

