class Solution:
    def modifyString(self, s: str) -> str:
        s = list("?"+s+"?")
        for i in range(1,len(s)-1):
            if s[i] == "?":
                for j in "abc":
                    if j != s[i-1] and j !=s[i+1]:
                        s[i] = j
        return "".join(s[1:-1])