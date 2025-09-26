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
        result = float('-inf')
        stack = [(root, False)]
        gain = {}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                leftgain = max(gain.get(node.left, 0), 0)
                rightgain = max(gain.get(node.right, 0), 0)
                cur = node.val + leftgain + rightgain
                result = max(cur, result)
                gain[node] = node.val + max(leftgain, rightgain)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return result
        