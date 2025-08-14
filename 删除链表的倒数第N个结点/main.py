# 快慢指针
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        first = head
        newhead = ListNode(0 , head)
        second = newhead
        # 可以考虑second向后一个找前驱结点  而不是first向前一个
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return newhead.next
            
        