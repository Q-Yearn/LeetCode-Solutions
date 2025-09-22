# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 原地修改不需要返回值
        if root is None:
            return
        tmp = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            tmp.append(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        length = len(tmp)
        if length > 1:
            for i in range(length-1):
                tmp[i].left = None
                tmp[i].right = tmp[i+1]
        



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 边遍历边改变指针
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 原地修改不需要返回值
        if root is None:
            return
        tmp = []
        stack = []
        stack.append(root)
        pre = None
        while stack:
            node = stack.pop()
            if pre:
                pre.left = None
                pre.right = node
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            pre = node
         