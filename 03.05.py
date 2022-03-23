class SortedStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.size = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        for i in self.s1[::-1]:
            if i < val:
                self.s2.append(i)
            else:
                break
            self.s1.pop()

        self.s1.append(val)

        # for i in self.s2[::-1]:
        #     self.s1.append(i)
        self.s1 += [i for i in self.s2[::-1]]

        self.s2 = []
        self.size += 1

    def pop(self):
        """
        :rtype: None
        """
        if self.size == 0:
            return None
        self.size -= 1
        self.s1.pop()
        return None

    def peek(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.s1[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
