from typing import *
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.pointy = defaultdict(list)
        self.xynum = defaultdict(int)

    def add(self, point: List[int]) -> None:
        if self.xynum[(point[0], point[1])] == 0:
            self.pointy[point[1]].append([point[0],point[1]])
        self.xynum[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for p in self.pointy[point[1]]:
            line = p[0] - point[0]
            if line == 0 :
                continue
            ans += self.xynum[(p[0], point[1])] * self.xynum[(point[0], point[1] - line)] * self.xynum[
                (p[0], point[1] - line)]
            ans += self.xynum[(p[0], point[1])] * self.xynum[(point[0], point[1] + line)] * self.xynum[
                (p[0], point[1] + line)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
