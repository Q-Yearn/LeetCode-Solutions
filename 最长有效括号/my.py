class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 0:
            return 0
        dp = [0] * m
        for i in range(1, m):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
                # 单独的一个')'不会入栈 所以不空只能是'('
                else:
                    if  i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                        pre = dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0
                        dp[i] = 2 + dp[i-1] + pre
        return max(dp)

        