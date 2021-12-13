from typing import *
n = 2

class Solution:
    def __init__(self):
        self.ans = set()
        self.watchlis = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None

    def check(self, hour , minute):
        if hour > 11 or minute > 59:
            return False
        else:
            return True

    def visit2time(self, visited):
        hour = 0
        minute = 0
        for i in range(0, 4):
            if visited[i]:
                hour += self.watchlis[i]
        for i in range(4, 10):
            if visited[i]:
                minute += self.watchlis[i]
        if hour > 11 or minute > 59:
            return False
        else:
            if minute<10:
                return str(hour) + ':' + str(0) + str(minute)
            return str(hour) + ':' + str(minute)

    def dfs(self, num, step, start):
        if step == num:
            time = self.visit2time(self.visited)
            if time:
                self.ans.add(time)
            return 0

        for i in range(start, len(self.visited)):
            if self.visited[i] == 0:
                self.visited[i] = 1
                self.dfs(num, step + 1, start + 1)
                self.visited[i] = 0

    def readBinaryWatch(self, num: int) -> List[str]:
        self.visited = [0]*len(self.watchlis)
        self.dfs(num, 0, 0)

        return list(self.ans)


if __name__ == '__main__':
    res = Solution()
    print(res.readBinaryWatch(n))