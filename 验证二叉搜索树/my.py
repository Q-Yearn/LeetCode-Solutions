# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 左子树的右节点还必须小于前一个父节点  右子树的左节点还必须大于前一个父节点
# 需要考虑多层关系  这只考虑了两层
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root, val, preval, is_left, pre_is_left):
            if root is None:
                return True
            if is_left:
                if not pre_is_left:
                    return root.val < val and root.val > preval and helper(root.left, root.val, val, 1, is_left) and helper(root.right, root.val, val, 0, is_left)
                else:
                    return root.val < val and helper(root.left, root.val, val, 1, is_left) and helper(root.right, root.val, val, 0, is_left)
            else:
                if pre_is_left:
                    return root.val > val and root.val < preval and helper(root.left, root.val, val, 1, is_left) and helper(root.right, root.val, val, 0, is_left) 
                else:
                    return root.val > val and helper(root.left, root.val, val, 1, is_left) and helper(root.right, root.val, val, 0, is_left) 
        return helper(root.left, root.val, root.val, 1, 1) and helper(root.right, root.val, root.val, 0, 0)
