from typing import *
num = 4

class Solution:
    def intToRoman(self, num: int) -> str:
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        ans = []
        for value, symbol in VALUE_SYMBOLS:
            while num >= value:
                num -= value
                ans.append(symbol)
                if num == 0:
                    break
        return "".join(ans)


if __name__ == '__main__':
    res = Solution()
    print(res.intToRoman(num))
