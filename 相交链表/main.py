# 字典
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
        tmp = set()
        m = headA
        while m is not None:
            tmp.add(m)
            m = m.next
        n = headB
        while n is not None:
            if n in tmp:
                return n
            n = n.next
        return None
# 双指针
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
        n = headB
        while m is not n:
            m = m.next if m is not None else headB
            n = n.next if n is not None else headA
        return m