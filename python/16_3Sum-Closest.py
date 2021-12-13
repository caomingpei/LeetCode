from typing import *
nums = [0,2,1,-3]
target = 1
INTMAX = 0x3f3f3f3f
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return []
        nums = sorted(nums)
        cur = INTMAX
        for i in range(n):
            if i> 0 and nums[i] == nums[i-1]: ## [0,0,0]
                continue
            Lp = i+1
            Rp = n-1
            if Lp > n-1 or Rp < 0 :
                return cur
            while Lp < Rp:
                midres = nums[i] + nums[Lp] + nums[Rp]
                if midres == target:
                    return target
                else:
                    if abs(target-midres) < abs(cur-target):
                        cur = midres
                    if midres > target:
                        Rp -= 1
                    elif midres < target:
                        Lp += 1

        return cur

if __name__ == '__main__':
    res = Solution()
    print(res.threeSumClosest(nums,target))