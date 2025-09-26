# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = float('-inf')
        def maxgain(root):
            if not root:
                return 0
            leftgain = max(maxgain(root.left), 0)
            rightgain = max(maxgain(root.right), 0)
            cur = root.val + leftgain + rightgain
            self.result = max(self.result, cur)
            return root.val + max(leftgain, rightgain)
        maxgain(root)
        return self.result
            
        