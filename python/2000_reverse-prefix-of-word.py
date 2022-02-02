from typing import *
from collections import deque

word = "a"
ch = "a"

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = word
        for i in range(len(word)):
            if word[i] == ch:
                cur = word[:i+1]
                ans = cur[::-1] + word[i+1:]
                return ans
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.reversePrefix(word,ch))