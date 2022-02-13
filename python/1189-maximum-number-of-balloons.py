from typing import *
from collections import defaultdict

text = "loonbalxballpoon"

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cal = [0 for _ in range(26)]
        ans = float('inf')
        for i in range(len(text)):
            char = text[i]
            cal[ord(char)-ord('a')] += 1
        for char in ['b','a','l','o','n']:
            if char == 'l' or char == 'o':
                ans = min(ans, cal[ord(char)-ord('a')]//2)
            ans = min(ans, cal[ord(char)-ord('a')])
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.maxNumberOfBalloons(text))