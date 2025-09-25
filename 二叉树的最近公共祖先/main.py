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
        self.result = None
        def helper(root, p, q):
            if not root:
                return False
            lson = helper(root.left, p, q)
            rson = helper(root.right, p, q)
            if  (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
                self.result = root
            return lson or rson or root.val == p.val or root.val == q.val
        helper(root, p, q)
        return self.result


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
        self.fa = {}
        def helper(root):
            if root.left:
                self.fa[root.left.val] = root
                helper(root.left)
            if root.right:
                self.fa[root.right.val] = root
                helper(root.right)
        # 用集合就行
        vi = {}
        self.fa[root.val] = None
        helper(root)
        while p:
            vi[p.val] = True
            p = self.fa[p.val]
        while q:
            if q.val in vi:
                return q
            q = self.fa[q.val]