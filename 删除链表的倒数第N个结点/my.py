# 或者循环两边 第一遍计数  第二遍删除   或者用栈也行
class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmp = []
        m = head
        while m:
            tmp.append(m)
            m = m.next
        
        length = len(tmp)
        
        if length == 1:  # 链表只有一个节点
            return None
        if n == length:  # 删除头节点
            return head.next
        if n == 1:  # 删除尾节点
            tmp[-2].next = None
        else:  # 删除中间节点
            tmp[-(n+1)].next = tmp[-(n-1)]
        
        return head