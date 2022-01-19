from typing import *
nums = [1,0,1,1]
k = 1


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys() and abs(dic[nums[i]] - i) <=k:
                return True
            dic[nums[i]] = i
        return False

if __name__ == '__main__':
    res = Solution()
    print(res.containsNearbyDuplicate(nums, k))

