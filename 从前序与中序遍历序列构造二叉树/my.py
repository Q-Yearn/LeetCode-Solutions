# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.num = 0
        def helper(left, right, num):
            if left > right:
                return None
            cur = left
            while cur <= right:
                if preorder[num] == inorder[cur]:
                    break
                cur += 1
            root = TreeNode(val = inorder[cur])
            self.num += 1
            root.left = helper(left, cur-1, self.num)
            root.right = helper(cur+1, right, self.num)
            return root
        root = helper(0, len(inorder)-1, 0)
        return root
        