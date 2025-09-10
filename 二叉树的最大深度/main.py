# 深度优先搜索  自己版本的简化
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 广度优先搜索
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None: return 0
        queue = deque([root])
        ans = 0
        while queue:
            sz = len(queue)
            while sz > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sz -= 1
            ans += 1
        return ans