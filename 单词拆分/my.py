class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word = set()
        for w in wordDict:
            word.add(w)
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j+1:i+1] in word:
                    dp[i] = True
                    break
            if s[:i+1] in word:
                dp[i] = True
        return dp[len(s)-1]



        