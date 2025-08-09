# 逆转指针
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        m = head
        if m is None:
            return None
        while m.next is not None:
            result.append(m)
            m = m.next
        n = m
        for i in  range (len(result)-1, -1, -1):
            n.next = result[i]
            n = result[i]
        n.next = None
        return m