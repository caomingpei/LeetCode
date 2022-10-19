from typing import *
students = [1,1,0,0]
sandwiches = [0,1,0,1]


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a1 = sum(students)
        a0 = len(students) - a1
        for s in sandwiches:
            if s == 0 and a0:
                a0 -= 1
            elif s == 1 and a1:
                a1 -= 1
            else:
                break
        return a0 + a1


if __name__ == '__main__':
    res = Solution()
    print(res.countStudents(students, sandwiches))