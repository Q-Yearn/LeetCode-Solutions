# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.result = []
        self.k = 0
        def helper(root):
            if not root:
                return None
            self.result.append(root.val)
            for i in range(0, len(self.result)-1):
                self.result[i] += root.val
                if self.result[i] == targetSum:
                    self.k += 1
            if self.result[-1] == targetSum:
                self.k += 1
            helper(root.left)
            helper(root.right)
            # 回溯一下
            self.result.pop()
            for i in range(0, len(self.result)):
                self.result[i] -= root.val
        helper(root)
        return self.k

        