# 超时
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        def climb(step):
            if step == n:
                self.res += 1
                return
            if step > n:
                return
            climb(step+1)
            climb(step+2)
        climb(0)
        return self.res

# 动态规划
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[1] = 1
        res[0] = 1
        for i in range(2, n+1):
            res[i] = res[i-2] + res[i-1]
        return res[n]
