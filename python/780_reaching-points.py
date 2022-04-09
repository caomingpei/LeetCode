from typing import *

sx = 3
sy = 7
tx = 3
ty = 4

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        while sx < tx != sy < ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True
        elif tx < ty and tx == sx:
            return ((ty - sy) % tx)==0
        elif tx > ty and ty == sy :
            return ((tx - sx) % ty) == 0
        else:
            return False


if __name__ == '__main__':
    res = Solution()
    print(res.reachingPoints(sx,sy,tx,ty))