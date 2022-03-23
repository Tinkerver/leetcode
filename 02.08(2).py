# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        i, j = head, head
        n = 0
        m = 0
        while i:
            j = head
            m = 0
            while j != i:
                j = j.next
                m = m + 1
            if m != n:
                return j

            i = i.next
            n = n + 1

        return None