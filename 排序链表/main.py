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
        def merge(head1, head2):
            tmphead = ListNode(0)
            tmp, tmp1, tmp2 = tmphead, head1, head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp2 = tmp2.next
                tmp = tmp.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            while tmp.next:
                tmp = tmp.next
            return tmphead.next, tmp
        
        if head is None:
            return None
        length = 0
        m = head
        while m:
            length += 1
            m = m.next
        
        sublength = 1
        tmphead = ListNode(0, head)
        while sublength < length:
            pre, cur = tmphead, tmphead.next
            while cur:
                head1 = cur
                for i in range(sublength-1):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                head2 = cur.next
                cur.next = None
                cur = head2
                for i in range(sublength-1):
                    # 注意这一步 考虑最后两个一组 第二组是None的情况
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                # 也是考虑最后两个一组 第二组是None的情况
                tmp = None
                if cur:
                    tmp = cur.next
                    cur.next = None
                merged, tail = merge(head1, head2)
                pre.next = merged
                pre = tail
                cur = tmp
            sublength *= 2
        return tmphead.next