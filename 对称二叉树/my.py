# 中序和一致不一定对称 必须实时比较左右子树
# 比如
#       1
#     2   3
#   3   2
class Solution(object):
    def __init__(self):
        self.tmp1 = []
        self.tmp2 = []
    def traversal1(self, root):
        if root is None:
            return
        self.traversal1(root.left)
        self.tmp1.append(root.val)
        self.traversal1(root.right)

    def traversal2(self, root):
        if root is None:
            return
        self.traversal2(root.right)
        self.tmp2.append(root.val)
        self.traversal2(root.left)
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """  
        self.traversal1(root)
        self.traversal2(root)
        if self.tmp1 == self.tmp2:
            return True
        else:
            return False
        有什么问题