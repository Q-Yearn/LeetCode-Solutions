# 快慢指针
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        
        tmp = head
        while tmp is not slow:
            tmp = tmp.next
            slow = slow.next
        return tmp