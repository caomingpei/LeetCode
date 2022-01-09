from typing import *
n = 2

releaseTimes = [9,29,49,50]
keysPressed = "cbcd"

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > maxTime or time == maxTime and key > ans:
                ans = key
                maxTime = time
        return ans



if __name__ == '__main__':
    res = Solution()
    print(res.slowestKey(releaseTimes,keysPressed))