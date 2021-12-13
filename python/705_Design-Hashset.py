from typing import *


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashprimes = 1001
        self.hashset = [[] for _ in range(self.hashprimes)]

    def hash(self, num):
        return num % self.hashprimes

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.hashset[hashkey]:
            return
        self.hashset[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.hashset[hashkey]:
            return
        self.hashset[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.hash(key)
        return key in self.hashset[hashkey]




if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.contains(1)
    obj.contains(3)
    obj.add(2)
    obj.contains(2)
    obj.remove(2)
    print(obj.contains(2))
