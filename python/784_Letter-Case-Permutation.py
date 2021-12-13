from typing import *
S = "a1b2"

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bit in range(1<<B):
            cur=""
            b = 0
            for letter in S:
                if letter.isalpha():
                    if (bit>>b) % 2 == 1:
                        cur += letter.upper()
                    else:
                        cur += letter.lower()
                    b += 1
                else:
                    cur += letter
            ans.append(cur)

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.letterCasePermutation(S))