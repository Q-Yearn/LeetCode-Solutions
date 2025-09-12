# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 二叉树的直径是指任意两节点的路径长度
# 不一定经过根节点
# 可能是左子树中两个节点
class Solution(object):
    def maxdepth(self, root):
        if root is None: return 0
        return max(self.maxdepth(root.left), self.maxdepth(root.right)) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxdepth(root.left) + self.maxdepth(root.right)