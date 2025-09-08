# “颜色标记法” 
# 兼具栈迭代方法的高效，又像递归方法一样简洁易懂
# 更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        WHITE, GRAY = 0, 1
        result = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                result.append(node.val)
        return result