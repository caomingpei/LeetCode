from typing import *
head = [4,2,1,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or head.next == None:
            return head

        current, length = head, 0
        while current:  # 求得链表长度
            current, length = current.next, length + 1

        root = ListNode(0)
        root.next = head
        intv = 1  # 每次合并的规模

        # 根据不同的链表切片规模，每一次都从头进行归并
        while intv < length:
            merge_point, current = root, root.next

            while current:  # 根据当前的合并规模，将链表内的链表切片两两归并

                # 获取当前需要归并的子链表 h1
                h1, intv_residue_1 = current, intv
                while intv_residue_1 and current:
                    current, intv_residue_1 = current.next, intv_residue_1 - 1
                if intv_residue_1:  # h2 在这种情况下不存在，所以本轮不需要合并
                    break

                # 获取当前需要归并的子链表 h2
                h2, intv_residue_2 = current, intv
                while intv_residue_2 and current:
                    current, intv_residue_2 = current.next, intv_residue_2 - 1

                len1, len2 = intv, intv - intv_residue_2  # len2 的长度可能比 intv 小

                while len1 and len2:  # 归并排序
                    if h1.val < h2.val:
                        merge_point.next, h1, len1 = h1, h1.next, len1 - 1
                    else:
                        merge_point.next, h2, len2 = h2, h2.next, len2 - 1
                    merge_point = merge_point.next

                if len1:  # 归并排序处理一下没有被归并的剩余值
                    merge_point.next = h1
                else:
                    merge_point.next = h2
                while len1 > 0 or len2 > 0:
                    merge_point, len1, len2 = merge_point.next, len1 - 1, len2 - 1

                merge_point.next = current  # h1 和 h2 的归并只是影响了链表的一部分，这里应该把归并后的链表切片跟原链表h2之后的部分拼起来

            intv *= 2

        return root.next


if __name__ == '__main__':
    res = Solution()
    print(res.sortList(head))