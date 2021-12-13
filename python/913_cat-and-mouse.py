class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def search(t, x, y):
            if t == int(len(graph)*2):
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            if t % 2 == 0:
                if any(search(t+1, xnext, y) == 1 for xnext in graph[x]):
                    return 1
                if any(search(t+1, xnext, y) == 0 for xnext in graph[x]):
                    return 0
                return 2
            else:
                if any(search(t+1, x, ynext) == 2 for ynext in graph[y] if ynext!= 0):
                    return 2
                if any(search(t+1, x, ynext) == 0 for ynext in graph[y] if ynext!= 0):
                    return 0
                return 1

        return search(0,1,2)
