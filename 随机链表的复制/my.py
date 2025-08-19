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
        random_index = []
        tmp_node = []
        result = []
        m = head
        while m:
            tmp_node.append(m)
            m = m.next
        m = head
        while m:
            if m.random is None:
                random_index.append(-1)
            else:
                idx = tmp_node.index(m.random)
                random_index.append(idx)
            m = m.next
        length = len(tmp_node)
        for i in range(length):
            node = Node(tmp_node[i].val)
            result.append(node)
        for i in range(length):
            if random_index[i] == -1:
                result[i].random = None
            else:
                result[i].random = result[random_index[i]]
            if i < length-1:
                result[i].next = result[i+1]
            else:
                result[i].next = None
        return result[0]
        