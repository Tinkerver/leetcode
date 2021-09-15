# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head.next

        while (p):
            j = p
            while (j.next):
                while j.next.val == p.val:
                    j.next = j.next.next
                    continue
                j = j.next
            p = p.next

        return head
