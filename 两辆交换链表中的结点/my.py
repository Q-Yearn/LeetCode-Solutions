# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        m = head
        n = head.next
        pre = None
        newhead = head.next
        while m and n:
            m.next = n.next
            n.next = m
            if pre:
                pre.next = n
            pre = m 
            m = m.next
            if m:
                n = m.next
            else:
                n = None
        return newhead
