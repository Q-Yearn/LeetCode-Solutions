# 左上角到右下角的过程中，我们需要移动 m+n−2 次
# 其中有 m−1 次向下移动，n−1 次向右移动
# 因此路径的总数，就等于从 m+n−2 次移动中选择 m−1 次向下移动的方案数
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = m + n - 2
        b = m - 1
        res = 1
        for i in range(1, m):
            res = res * (a - b + i) // i
        return res
            