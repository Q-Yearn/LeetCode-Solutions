# DP
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            num = 1
            while num * num <= i:
                dp[i] = min(dp[i], dp[i-num*num]+1)
                num += 1
        return dp[n]
    

# 拉格朗日四平方和定理
# 任何正整数都可以表示为至多 4 个平方数之和
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if int((n**0.5))**2 == n:
            return 1

        tmp = n
        while tmp % 4 == 0:
            tmp //= 4
        if tmp % 8 == 7:
            return 4

        for i in range(1, int(n**0.5)+1):
            remain = n - i**2
            if int((remain**0.5))**2 == remain:
                return 2
                
        return 3
          