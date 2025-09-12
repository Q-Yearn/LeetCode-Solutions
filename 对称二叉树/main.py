# 递归
class Solution(object):
    def check(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """  
        if root is None:
            return True
        return self.check(root.left, root.right)

# 迭代
from collections import deque
class Solution(object):
    def check(self, left, right):
        q = deque()
        q.append(left)
        q.append(right)
        while q:
            u = q.popleft()
            v = q.popleft()
            if not u and not v: continue
            # 等价  if not u aor not v or u.val != v.val: return False
            # 只有u和v同时不空才会执行u.val=v.val
            if not u or not v: return False
            if u and v and u.val != v.val: return False
            q.append(u.left)
            q.append(v.right)
            q.append(u.right)
            q.append(v.left)
        return True
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """  
        if root is None:
            return True
        return self.check(root.left, root.right)