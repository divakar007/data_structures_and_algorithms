import random
class RandomizedSet(object):

    def __init__(self):
        self.set_d = set()

        self.n = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.set_d:
            return False
        self.set_d.add(val)
        self.n += 1
        return True 

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.set_d:
            self.set_d.remove(val)
            self.n -= 1
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        ind = random.randint(0, self.n-1)
        return list(self.set_d)[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()