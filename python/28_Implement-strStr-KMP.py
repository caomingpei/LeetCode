from typing import *
haystack = "hello"
needle = "ll"

class Solution:
    def KMP(self,s ,p):
        def getNext(p):
            mynext = [0 for i in range(len(p)+1)]
            mynext[0] = -1
            i, j = 0, -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    mynext[i] = j
                else:
                    j = mynext[j]
            return mynext
        mynext = getNext(p)
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:
                i+=1
                j+=1
            else:
                j = mynext[j]
        if j == len(p):
            return i-j
        else:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return self.KMP(haystack,needle)

if __name__ == '__main__':
    res = Solution()
    print(res.strStr(haystack, needle))
