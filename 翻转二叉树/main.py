from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root