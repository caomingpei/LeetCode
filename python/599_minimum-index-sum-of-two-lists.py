from typing import *

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        minNum = float("inf")
        m1,m2 = dict(),dict()
        for i, v in enumerate(list1):
            m1[v] = i
        for i, v in enumerate(list2):
            m2[v] = i
        for i, v in enumerate(list1):
           if v in m2.keys():
               cur = i+m2[v]
               if cur < minNum:
                   minNum = cur
                   ans = [v]
               elif cur == minNum:
                   ans.append(v)
        return ans



if __name__ == '__main__':
    res = Solution()
    print(res.findRestaurant(list1,list2))