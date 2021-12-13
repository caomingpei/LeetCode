class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        queue_in = []
        queue_out = []
        self.queue_in = queue_in
        self.queue_out = queue_out

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue_out):
            ans = self.queue_out.pop()
        else:
            while(len(self.queue_in)):
                cur = self.queue_in.pop()
                self.queue_out.append(cur)
            ans = self.queue_out.pop()

        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue_out):
            ans = self.queue_out[-1]
        else:
            while (len(self.queue_in)):
                cur = self.queue_in.pop()
                self.queue_out.append(cur)
            ans = self.queue_out[-1]
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(len(self.queue_in) or len(self.queue_out)):
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
print(myQueue.push(1))
print(myQueue.push(2))
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
