# 矩阵快速幂
class Solution:
    def multiply(self, a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

    def matrixPow(self, a, n):
        # 单位矩阵
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.multiply(ret, a)
            n >>= 1
            a = self.multiply(a, a)
        return ret

    def climbStairs(self, n):
        base = [[1, 1], [1, 0]]
        res = self.matrixPow(base, n)
        return res[0][0]

# 数列通项公式
import math

class Solution:
    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        fibn = math.pow(phi, n + 1) - math.pow(psi, n + 1)
        return int(fibn // sqrt5)