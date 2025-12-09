# min(m, n) - dp[m][n] 不是需要替换的次数
# 因为可能会发生错位
# abc adc可以
# sea eat就不可以
# 实际上如果只要求插入和删除操作  是需要求公共最长子序列
# 那么最少操作次数就为 m + n - dp[m][n]
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        cnt1 = m - n if m > n else n - m
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return cnt1 + (n - dp[m][n] if m > n else n - dp[m][n])
