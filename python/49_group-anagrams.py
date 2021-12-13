from typing import *
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
class Solution:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    def hash(self, lis):
        MOD = int(1e9 + 7)
        ans = 0
        for i in range(26):
            ans *= self.prime[i]
            ans += lis[i]
            ans %= MOD
        return ans

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for str in strs:
            curlis = [0]*26
            for i in range(len(str)):
                curlis[ord(str[i])-ord('a')] += 1
            num = self.hash(curlis)
            if num not in dic.keys():
                dic[num]= [str]
            else:
                dic[num].append(str)
        ans = []
        for i in dic.keys():
            ans.append(dic[i])
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.groupAnagrams(strs))