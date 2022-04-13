from typing import *
import random


class RandomizedSet:
    def __init__(self):
        self.num = []
        self.num2ind = dict()

    def insert(self, val: int) -> bool:
        if val not in self.num2ind.keys():
            self.num2ind[val] = len(self.num)
            self.num.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.num2ind.keys():
            return False
        index, lastv = self.num2ind[val], self.num[-1]
        self.num[index], self.num2ind[lastv] = lastv, index
        self.num.pop()
        self.num2ind.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.num)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()