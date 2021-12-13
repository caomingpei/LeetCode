from typing import *
nums = [2,7,11,15]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i in range(len(nums)):
            x = nums[i]
            if target-x not in hashtable:
                hashtable[x] = i
            else:
                return [hashtable[target-x],i]

if __name__ == '__main__':
    res = Solution()
    print(res.twoSum(nums,target))