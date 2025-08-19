# 递归
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.chache_node = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 不能放这啊肯定
        # chache_node = {}
        if head is None:
            return None
        if head not in self.chache_node:
            newnode = Node(head.val)
            self.chache_node[head] = newnode
            newnode.next = self.copyRandomList(head.next)
            newnode.random = self.copyRandomList(head.random)
        return self.chache_node[head]        


# 结点拆分
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        m = head
        while m:
            node = Node(m.val)
            node.next = m.next
            m.next = node
            m = m.next.next
        m = head
        while m:
            node = m.next
            node.random = m.random.next if m.random else None
            m = m.next.next
        newhead = head.next
        m = head
        while m:
            node = m.next
            m.next = m.next.next
            node.next = node.next.next if node.next else None
            m = m.next
        return newhead 

 