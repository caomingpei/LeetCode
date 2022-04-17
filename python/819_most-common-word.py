from typing import *
from collections import defaultdict

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = defaultdict(int)
        word = ""
        for i in range(len(paragraph) + 1):
            if i < len(paragraph) and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                cnt[word] += 1
                word = ""
        for ban in banned:
            cnt[ban] = 0
        mmax = -1
        ans = 0
        for i in cnt.keys():
            if cnt[i] > mmax:
                ans = i
                mmax = cnt[i]
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.mostCommonWord(paragraph,banned))