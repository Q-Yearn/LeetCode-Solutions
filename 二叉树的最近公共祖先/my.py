# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = []
        path2 = []
        self.flag = 0
        def helper(root, node, path):
            if self.flag == 1:
                return 
            if not root:
                return 
            path.append(root)
            if root is node:
                self.flag = 1
            helper(root.left, node, path)
            helper(root.right, node, path)
            if self.flag == 0:
                path.pop()
        helper(root, p, path1)
        self.flag = 0
        helper(root, q, path2)
        if len(path1) < len(path2):
            for i in range(len(path1)-1, -1, -1):
                if path1[i] in path2:
                    return path1[i]
        else:
            for i in range(len(path2)-1, -1, -1):
                if path2[i] in path1:
                    return path2[i]  