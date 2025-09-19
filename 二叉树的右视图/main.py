# 深度优先搜索
# 每次先访问右子树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = {}
        self.max_depth = -1
    def helper(self, root, depth):
        if not root:
            return
        self.max_depth = max(self.max_depth, depth)
        if depth not in self.result:
            self.result[depth] = root.val
        self.helper(root.right, depth+1)
        self.helper(root.left, depth+1)
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.helper(root, 0)
        return [self.result[depth] for depth in range(self.max_depth+1)]
        