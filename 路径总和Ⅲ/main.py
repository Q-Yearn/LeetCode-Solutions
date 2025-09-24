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
        # 没必要存路径和  存路径然后遍历就好了
        self.path = []
        self.k = 0
        def helper(root):
            if not root:
                return None
            self.path.append(root.val)
            tmpsum = 0
            for i in range(len(self.path)-1, -1, -1):
                tmpsum += self.path[i]
                if tmpsum == targetSum:
                    self.k += 1
            helper(root.left)
            helper(root.right)
            # 回溯一下
            self.path.pop()
        helper(root)
        return self.k



# 前缀和
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
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        def helper(root, cur):
            if not root:
                return 0
            cur += root.val
            ret = 0
            ret += prefix[cur-targetSum]
            prefix[cur] += 1
            ret += helper(root.left, cur)
            ret += helper(root.right, cur)
            prefix[cur] -= 1
            return ret
        ret = helper(root, 0)
        return ret
        