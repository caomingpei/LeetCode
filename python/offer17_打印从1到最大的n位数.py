from typing import *
n = 3

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        nums = [0] * n
        self.nine = 0
        self.start = n-1
        def dfs(x):
            if x == n:
                s = ''.join(nums[self.start:])
                res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                nums[x] = str(i)
                dfs(x+1)
            self.nine -= 1
        dfs(0)
        return res[1:]

if __name__ == '__main__':
    res = Solution()
    print(res.printNumbers(n))
