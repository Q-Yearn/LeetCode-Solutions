# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 迭代
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderindex = 0
        for i in range(1, len(preorder)):
            preorderval = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderindex]:
                node.left = TreeNode(preorderval)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderindex]:
                    node = stack.pop()
                    inorderindex += 1
                node.right = TreeNode(preorderval)
                stack.append(node.right)
        return root