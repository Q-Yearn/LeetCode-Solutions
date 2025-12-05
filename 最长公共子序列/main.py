# 空间优化
# pre代表dp[i-1][j-1] 
# dp[j]代表dp[i-1][j] 
# dp[j-1]代表dp[i][j-1]
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text2
        m = len(text1)
        n = len(text2)
        dp = [0] *  (n+1)
        for i in range(1, m+1):
            pre = 0
            for j in range(1, n+1):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = tmp
        return dp[n]