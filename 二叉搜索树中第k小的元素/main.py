# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MyBst:
    def __init__(self, root):
        self.root = root
        self.node_num = {}
        self.count_node_num(root)
    def count_node_num(self, root):
        if not root:
            return 0
        self.node_num[root] = 1 + self.count_node_num(root.left) + self.count_node_num(root.right)
        return self.node_num[root]
    def kth_smallest(self, k):
        root = self.root
        while root:
            count = self.node_num[root.left] if root.left else 0
            if count == k-1:
                return root.val
            elif count < k-1:
                root = root.right
                k = k - count - 1
            else:
                root = root.left
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        bst = MyBst(root)
        return bst.kth_smallest(k)
