# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 没必要每次创建新结点  用原来的就行
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        m = list1
        n = list2
        pre = ListNode()
        x = pre
        while m is not None and n is not None:
            newhead = ListNode()
            if m.val <= n.val:
                newhead.val = m.val
                m = m.next
            else:
                newhead.val = n.val
                n = n.next
            x.next = newhead
            x = x.next
        while m is not None:
            newhead = ListNode()
            newhead.val = m.val
            x.next = newhead
            x = x.next
            m = m.next
        while n is not None:
            newhead = ListNode()
            newhead.val = n.val
            x.next = newhead
            x = x.next
            n = n.next
        return pre.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        m = list1
        n = list2
        pre = ListNode()
        x = pre
        while m is not None and n is not None:
            if m.val <= n.val:
                x.next = m
                m = m.next
            else:
                x.next = n
                n = n.next
            x = x.next
        x.next = m if m is not None else n
        return pre.next

