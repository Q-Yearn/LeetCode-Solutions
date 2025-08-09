# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        m = head
        while m is not None:
            tmp.append(m)
            m = m.next
        n = len(tmp)
        for i in range(n // 2):
            if tmp[i].val != tmp[n-1-i].val:
                return False
        return True