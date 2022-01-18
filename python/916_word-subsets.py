from typing import *
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        chrlis = [0 for _ in range(26)]
        for i in range(len(words2)):
            w2 = words2[i]
            cur = [0 for _ in range(26)]
            for j in range(len(w2)):
                cur[ord(w2[j])-ord('a')] +=1
            for k in range(26):
                chrlis[k] = max(cur[k],chrlis[k])

        ans = []
        for i in range(len(words1)):
            w1 = words1[i]
            cur = [0 for _ in range(26)]
            for j in range(len(w1)):
                cur[ord(w1[j])-ord('a')] += 1
            flag = True
            for k in range(26):
                if cur[k] < chrlis[k]:
                    flag = False
                    break
            if flag:
                ans.append(w1)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.wordSubsets(words1, words2))

