# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        mystack = deque()
        while(head != None):
            mystack.append(head.val)
            head = head.next
        ans = []
        while len(mystack):
            ans.append(mystack[-1])
            mystack.pop()
        return ans