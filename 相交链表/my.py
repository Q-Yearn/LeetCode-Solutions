# 超时了
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        m = headA
        # 推荐使用 is not None比较
        while m != None:
            n = headB
            while n != None:
                # m is n
                if m == n:
                    return m
                n = n.next
            m = m.next
        return None