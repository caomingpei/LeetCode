from typing import *

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashprime = 1001
        self.hashmap = [[] for _ in range(self.hashprime)]


    def hash(self, num):
        return num % self.hashprime

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = self.hash(key)
        self.remove(key)
        self.hashmap[hashkey].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = self.hash(key)
        for ob in self.hashmap[hashkey]:
            if ob[0] == key:
                return ob[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = self.hash(key)
        for ob in self.hashmap[hashkey]:
            if ob[0] == key:
                self.hashmap[hashkey].remove(ob)



if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.get(3)
    obj.put(2, 1)
    obj.get(2)
    obj.remove(2)
    obj.get(2)