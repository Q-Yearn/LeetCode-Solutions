from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelhelper(self, root, result, level):
        if root is None:
            return
        if len(result) < level:
            result.append([])
        result[level-1].append(root.val)
        self.levelhelper(root.left, result, level+1)
        self.levelhelper(root.right, result, level+1)

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.levelhelper(root, result, 1)
        return result
        