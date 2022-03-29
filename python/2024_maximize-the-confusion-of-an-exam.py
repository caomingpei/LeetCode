from typing import *
from collections import deque

answerKey = "TTFF"
k = 2

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxChar(char):
            left, ans, sunum = 0, 0, 0
            for right in range(len(answerKey)):
                sunum += (answerKey[right] != char)
                while sunum > k:
                    sunum -= (answerKey[left] != char)
                    left += 1
                ans = max(ans, right-left+1)
            return ans

        return max(maxChar("T"), maxChar("F"))

if __name__ == '__main__':
    res = Solution()
    print(res.maxConsecutiveAnswers(answerKey, k))