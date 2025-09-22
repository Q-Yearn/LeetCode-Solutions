# 对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点
# 将当前节点的右子节点赋给前驱节点的右子节点
# 然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空
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
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                cur.left = None
                pre.right = cur.right
                cur.right = nxt
            cur = cur.right
                
        
        