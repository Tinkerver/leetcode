# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i, j = 0, 0
        tmpA, tmpB = headA, headB
        while tmpA:
            i = i + 1
            tmpA = tmpA.next
        while tmpB:
            j = j + 1
            tmpB = tmpB.next
        tmpA, tmpB = headA, headB
        if i < j:
            tmp = j - i
            while tmp:
                tmpB = tmpB.next
                tmp = tmp - 1
        elif i > j:
            tmp = i - j
            while tmp:
                tmpA = tmpA.next
                tmp = tmp - 1

        while tmpA and tmpB:
            if tmpA == tmpB:
                return tmpA
            tmpA=tmpA.next
            tmpB=tmpB.next

        return None