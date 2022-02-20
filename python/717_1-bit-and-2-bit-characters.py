from typing import *

bits = [1, 0, 0]

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i<n-1:
            i += bits[i] +1
        return i == n-1


if __name__ == '__main__':
    res = Solution()
    print(res.isOneBitCharacter(bits))