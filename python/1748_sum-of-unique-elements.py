from typing import *
nums = [1,2,3,2]


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        state = {}
        for num in nums:
            if num not in state:
                ans += num
                state[num] = 1
            elif state[num] == 1:
                ans -= num
                state[num] = 2
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.sumOfUnique(nums))