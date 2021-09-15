class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a=[]
        self.b=[]


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)
        for i in self.a[::-1]:
            self.b.append(i)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp=self.b.pop()
        tmp_l=[]
        for i in self.a[1:]:
            tmp_l.append(i)
        self.a=tmp_l
        return tmp


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.a)==0