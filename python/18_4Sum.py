from typing import *
nums = [1, 0, -1, 0, -2, 2]
target = 0

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        hashtable = {}
        n = len(nums)
        res = []
        for j in range(n-1,2,-1):
            if j < n-1 and nums[j] == nums[j+1]:
                continue
            if 4*nums[j] < target:
                break
            if nums[j] + 3*nums[0] > target:
                continue
            for i in range(j-1,1,-1):
                if i < j-1 and nums[i] == nums[i+1]:
                    continue
                if nums[j] + 3*nums[i] <target:
                    break
                if nums[j] + nums[i] + 2*nums[0] > target:
                    continue
                hashtable.setdefault(nums[i]+nums[j],[]).append((i,j))
        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if 4* nums[i] > target:
                break
            if nums[i] + 3*nums[-1] < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + 3*nums[j] > target:
                    break
                if nums[i] + nums[j] + 2*nums[-1] < target:
                    continue
                for index, indey in hashtable.get(target-nums[i]-nums[j],[]):
                    if j < index:
                        res.append([nums[i],nums[j],nums[index],nums[indey]])
        return res



if __name__ == '__main__':
    res = Solution()
    print(res.fourSum(nums,target))