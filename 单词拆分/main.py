# 优化版
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        m = len(s)
        dp = [False] * (m+1)
        dp[0] = True
        for i in range(1, m+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[m]


# 记忆化搜索
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        tmp = {}
        def dfs(start):
            if start == len(s):
                return True
            
            if start in tmp:
                return tmp[start]
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and dfs(end):
                    tmp[start] = True
                    return True
            tmp[start] = False
            return False

        return dfs(0)