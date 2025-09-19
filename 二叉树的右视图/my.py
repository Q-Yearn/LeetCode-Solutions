# 深度优先搜索
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if size == 1:
                    result.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
        return result
        