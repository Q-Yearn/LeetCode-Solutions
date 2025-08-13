# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 模拟
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        m = l1
        n = l2
        newl = ListNode()
        x = newl
        flag = 0
        while m is not None and n is not None:
            if flag:
                cur_sum = m.val + n.val + 1
                flag = 0
            else:
                cur_sum = m.val + n.val
            if cur_sum >= 10:
                flag = 1
                cur_sum -= 10
            cur = ListNode()
            cur.val = cur_sum
            x.next = cur
            x = x.next
            m = m.next
            n = n.next
        while m is not None:
            if flag:
                cur_sum = m.val + 1
                flag = 0
                if cur_sum >= 10:
                    cur_sum -= 10
                    flag = 1    
            else:
                cur_sum = m.val
            cur = ListNode()
            cur.val = cur_sum
            x.next = cur
            x = x.next
            m = m.next
        while n is not None:
            if flag:
                cur_sum = n.val + 1
                flag = 0
                if cur_sum >= 10:
                    cur_sum -= 10
                    flag = 1    
            else:
                cur_sum = n.val
            cur = ListNode()
            cur.val = cur_sum
            x.next = cur
            x = x.next
            n = n.next
        if flag:
            cur = ListNode()
            cur.val = 1
            x.next = cur
        return newl.next

            