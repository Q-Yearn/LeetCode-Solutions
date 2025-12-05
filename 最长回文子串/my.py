# 暴力法  超时
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def judge(substring):
            return substring == substring[::-1]
        m = len(s)
        maxlen = 1
        res = s[0]
        for i in range(m):
            for j in range(i-1,-1,-1):
                substring =  s[j:i+1]
                if judge(substring):
                    if len(substring) > maxlen:
                        maxlen = len(substring)
                        res = substring
        return res
        