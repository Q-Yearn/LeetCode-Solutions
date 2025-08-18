# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head, tail):
        # tail为下一个子链的头
        pre = None
        cur = head
        newhead = None
        while cur is not tail:
            if cur.next is tail:
                newhead = cur
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return newhead, head

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 重新再前面加一个头节点  就不用记录是不是第一个子链了
        newhead = ListNode()
        newhead.next = head
        pre = newhead
        while head:
            cur_head = head
            for i in range(k):
                if head is None:
                    pre.next = cur_head
                    return newhead.next
                head = head.next
            cur_tail = head
            reverse_head, reverse_tail = self.reverse(cur_head, cur_tail)
            pre.next = reverse_head
            pre = reverse_tail
        return newhead.next

        