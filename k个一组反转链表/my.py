# 太难想了
# 思路是对的 也只需要个常数个中间变量  只不过可以把每次循环写成一个子函数，返回头和尾 可能更好想一点 就不用记录了
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        count = 0
        m = head
        while m:
            count += 1
            m = m.next
        cnt = count // k
        pre = None
        cur = head
        newhead = None
        cur_head = None
        pre_head = None
        for i in range(cnt):
            j = 1
            cur_tail = pre_head
            pre_head = cur
            while j <= k:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
                if j == k:
                    if i == 0:
                        newhead = pre
                    else:
                        cur_head = pre
                j += 1
            if i >= 1:
                cur_tail.next = cur_head
        pre_head.next = cur
        return newhead

        