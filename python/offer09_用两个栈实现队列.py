class CQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def appendTail(self, value: int) -> None:
        self.stackin.append(value)

    def deleteHead(self) -> int:
        if len(self.stackout):
            ans = self.stackout[-1]
            self.stackout.pop()
            return ans
        elif len(self.stackin):
            while len(self.stackin):
                cur = self.stackin[-1]
                self.stackout.append(cur)
                self.stackin.pop()
            ans = self.stackout[-1]
            self.stackout.pop()
            return ans
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()