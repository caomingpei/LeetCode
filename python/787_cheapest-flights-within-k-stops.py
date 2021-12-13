from typing import *
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        maxprice = float("inf")
        mat = [[maxprice for _ in range(k+1)] for _ in range(n)]

        for i in range(k+1):
            mat[src][i] = 0
        for cursrc, curdst, price in flights:
            if cursrc == src:
                mat[curdst][0] = price

        for cnt in range(1, k+1):
            for cursrc, curdst, price in flights:
                if mat[cursrc][cnt-1] != maxprice:
                    mat[curdst][cnt] = min(mat[cursrc][cnt-1] + price, mat[curdst][cnt])

        return mat[dst][k] if mat[dst][k] != maxprice else -1

if __name__ == '__main__':
    res = Solution()
    print(res.findCheapestPrice(n,edges,src,dst,k))