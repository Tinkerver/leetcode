class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = head
        b = head
        while (b.next != None and b.next.next != None):
            a = a.next
            b = b.next.next
        return a
