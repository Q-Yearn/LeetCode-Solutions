# 和上一个题思路差不多
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = set()
        m = head
        while m is not None:
            if m in tmp:
                return m
            else:
                tmp.add(m)
            m = m.next
        return None