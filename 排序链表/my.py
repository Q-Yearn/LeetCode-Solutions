# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        tmp = []
        while head:
            tmp.append(head)
            head = head.next
        tmp.sort(key=lambda x:x.val)
        length = len(tmp)
        for i in range(length-1):
            tmp[i].next = tmp[i+1]
        tmp[length-1].next = None
        return tmp[0]
        
            