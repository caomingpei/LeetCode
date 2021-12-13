from typing import *
nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3:
            return []
        nums = sorted(nums)
        res =[]
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            Lp = i+1
            Rp = n-1
            while Lp < Rp:
                midres = nums[i]+nums[Lp]+nums[Rp]
                if midres == 0:
                    res.append([nums[i],nums[Lp],nums[Rp]])
                    while Lp < Rp and nums[Lp] == nums[Lp+1]:
                        Lp += 1
                    while Lp < Rp and nums[Rp] == nums [Rp-1]:
                        Rp -= 1
                    Lp += 1
                    Rp -= 1
                elif midres > 0:
                    Rp -= 1
                elif midres < 0:
                    Lp += 1
        return res

if __name__ == '__main__':
    res = Solution()
    print(res.threeSum(nums))

