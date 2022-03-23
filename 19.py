import numba


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = head
        b = head
        for i in range(n):
            b = b.next
        if b==None:
            head=head.next
            return head
        while b.next != None:
            a = a.next
            b = b.next
        a.next = a.next.next
        return head
