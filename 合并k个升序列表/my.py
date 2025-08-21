# 比较慢了
# 还有一个是办法是  合并一个 再进行下一个
# 比上一个改进一点的方法是  分治  两两合并
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        newhead = ListNode(0)
        cur = newhead
        while any(sublist for sublist in lists):
            tmp = float('inf')
            tmp_node = None
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < tmp:
                        tmp = lists[i].val
                        tmp_node = lists[i]
                        idx = i
            cur.next = tmp_node
            cur = cur.next
            lists[idx] = lists[idx].next
        return newhead.next

