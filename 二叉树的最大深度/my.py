# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxdepth = 0
    def search(self, root, depth):
        if root is None:
            self.maxdepth = max(self.maxdepth, depth)
        else:
            depth += 1
            self.search(root.left, depth)
            self.search(root.right, depth)
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.search(root, 0)
        return self.maxdepth
        