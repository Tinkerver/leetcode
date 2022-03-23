class StackOfPlates:

    def __init__(self, cap: int):
        self.s = []
        self.len = cap

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            tmp = []
            tmp.append(val)
            self.s.append(tmp)
        elif len(self.s[-1]) < self.len:
            self.s[-1].append(val)
        elif len(self.s[-1]) == self.len:
            tmp = []
            tmp.append(val)
            self.s.append(tmp)

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1
        tmp = self.s[-1].pop()
        if len(self.s[-1]) == 0:
            self.s.pop()
        return tmp

    def popAt(self, index: int) -> int:
        if len(self.s) < index:
            return -1
        tmp = self.s[index].pop()
        if len(self.s[index]) == 0:
            self.s.pop(index)
        return tmp
