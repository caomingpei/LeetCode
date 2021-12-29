from typing import *
wordsLis = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.flag = False

    def insert(self, word: str):
        nod = self
        for ch in word:
            cnum = ord(ch) - ord('a')
            if not nod.child[cnum]:
                nod.child[cnum] = Trie()
            nod = nod.child[cnum]
        nod.flag = True

    def find(self, word):
        if word == "":
            return True
        nod = self
        for i in range(len(word)):
            cnum = ord(word[i]) - ord('a')
            nod = nod.child[cnum]
            if not nod:
                return False
            elif nod.flag == True and self.find(word[i+1:]):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans = []
        tree = Trie()
        for i in range(len(words)):
            word = words[i]
            if word == "":
                continue
            elif tree.find(word):
                ans.append(word)
            else:
                tree.insert(word)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.findAllConcatenatedWordsInADict(wordsLis))

