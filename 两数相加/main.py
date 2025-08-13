# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 递归
class Solution(object):
    def add_two(self, l1, l2, carry=0):
        if l1 is None and l2 is None and carry == 0:
            return None
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        cur_sum = num1 + num2 + carry
        newNode = ListNode(val=cur_sum%10)
        newNode.next = self.add_two(l1.next if l1 else None, l2.next if l2 else None, cur_sum // 10)
        return newNode
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newhead = self.add_two(l1, l2)
        return newhead

            