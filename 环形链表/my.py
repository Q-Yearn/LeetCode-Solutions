# 双循环遍历一个一个找当前结点是不是环的开头  不正确 因为如果不是当前结点是环  会死循环
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        count = {}
        count[head] = 1
        m = head
        while m.next is not None:
            if m.next not in count:
                count[m.next] = 1
            else:
                count[m.next] += 1
            if count[m.next] == 2:
                return True
            m = m.next
        return False

# 其实没必要计数  只需要访问该结点的时候  看看在不在字典中即可
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = set()
        m = head
        while m is not None:
            if m not in tmp:
                tmp.add(m)
            else:
                return True
            m = m.next
        return False

