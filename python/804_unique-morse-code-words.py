from typing import *

words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chr2morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        s = set()
        for word in words:
            cur = ""
            for ch in word:
                cur += chr2morse[ord(ch)-ord("a")]
            s.add(cur)
        return len(s)


if __name__ == '__main__':
    res = Solution()
    print(res.uniqueMorseRepresentations(words))