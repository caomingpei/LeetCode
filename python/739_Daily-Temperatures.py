from typing import *
temperatures = [55,38,53,81,61,93,97,32,43,78]

class Solution:
    stack = []
    ans = []
    def init(self):
        self.stack = []
        self.ans = []

    def push(self,temp_pair):
        if len(self.stack) > 0 :
            top_pair = self.stack[-1]
            while top_pair[0] < temp_pair[0]:
                self.stack.pop()
                self.ans[top_pair[1]] = temp_pair[1] - top_pair[1]
                if len(self.stack) > 0:
                    top_pair = self.stack[-1]
                else:
                    break
            self.stack.append(temp_pair)
        else:
            self.stack.append(temp_pair)

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        self.init()
        self.ans = [0]*len(T)
        for i in range(len(T)):
            self.push((T[i],i))
        return self.ans

if __name__ == '__main__':
    res = Solution()
    print(res.dailyTemperatures(temperatures))