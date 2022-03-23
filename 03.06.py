class AnimalShelf(object):

    def __init__(self):
        self.cat = []
        self.dog = []

    def enqueue(self, animal):
        """
        :type animal: List[int]
        :rtype: None
        """
        if animal[1] == 0:
            self.cat.append(animal)
        else:
            self.dog.append(animal)

    def dequeueAny(self):
        """
        :rtype: List[int]
        """

        if len(self.cat) == 0:
            if len(self.dog) == 0:
                return [-1, -1]
            else:
                return self.dog.pop(0)
        else:
            if len(self.dog) == 0:
                return self.cat.pop(0)
            else:
                if self.dog[0][0] < self.cat[0][0]:
                    return self.dog.pop(0)
                else:
                    return self.cat.pop(0)

    def dequeueDog(self):
        """
        :rtype: List[int]
        """
        if len(self.dog) == 0:
            return [-1, -1]
        else:
            return self.dog.pop(0)

    def dequeueCat(self):
        """
        :rtype: List[int]
        """
        if len(self.cat) == 0:
            return [-1, -1]
        else:
            return self.cat.pop(0)

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
