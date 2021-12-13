from typing import *

words= ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

class Word:
    def __init__(self, word, feq):
        self.word = word
        self.feq = feq

    def __lt__(self, other):
        if self.feq != other.feq:
            return self.feq < other.feq
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections, heapq
        cnt = collections.Counter(words)
        heap = []
        for word, feq in cnt.items():
            heapq.heappush(heap, Word(word, feq))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]


if __name__ == '__main__':
    res = Solution()
    print(res.topKFrequent(words, k))