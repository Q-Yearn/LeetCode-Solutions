# 递归 太难想了
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.m = head
        def reverse_check(current_node):
            if current_node is not None:
                if not reverse_check(current_node.next):
                    return False
                if current_node.val != self.m.val:
                    return False 
                self.m = self.m.next
            return True
        return reverse_check(head)    

# 找到链表前半部分和后半部分  然后后半部分反转  比较  然后再复原链表