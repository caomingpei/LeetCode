from typing import *

digits = "23"

class Solution:
    def init(self):
        tup = ("0", "!@#", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
        self.num2char = tup

    def letterCombinations(self, digits: str) -> List[str]:
        self.init()
        N = len(digits)
        self.ans = []
        if N == 0:
            return self.ans

        def dfs(i,str):
            if i == N:
                self.ans.append(str)
                return
            curlis = self.num2char[int(digits[i])]
            for chr in curlis:
                dfs(i+1, str + chr)

        dfs(0, "")
        return self.ans

if __name__ == '__main__':
    res = Solution()
    print(res.letterCombinations(digits))