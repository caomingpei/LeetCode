from typing import *

num1 = "1+-1i"
num2 = "1+-1i"

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = num1.split("+")
        r1, i1 = int(r1), int(i1[:-1])
        r2, i2 = num2.split("+")
        r2, i2 = int(r2),int(i2[:-1])
        r = r1*r2 - i1*i2
        i = r1*i2 + r2*i1
        return str(r)+"+"+str(i)+"i"

if __name__ == '__main__':
    res = Solution()
    print(res.complexNumberMultiply(num1,num2))