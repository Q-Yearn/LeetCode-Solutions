# 动态规划
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m < 2:
            return s
        dp = [[False for _ in range(m)] for _ in range(m)]

        for i  in range(m):
            dp[i][i] = True
        
        start = 0
        maxlen = 1
        for length in range(2, m+1):
            for i in range(m):
                j = i + length - 1
                if j >= m:
                    break
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                if dp[i][j] and length > maxlen:
                    start = i
                    maxlen = length
        
        return s[start:start+maxlen]
        

# 中心扩散法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m == 0:
            return ""
        def extend(left, right):
            while left >= 0 and right < m and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ""
        for i in range(m):
            s1 = extend(i, i)
            s2 = extend(i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res


# 中心扩散法改进版 Manacher算法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(list(s)) + '#'
        m = len(s)
        def expend(left, right):
            while left >= 0 and right < m and s[left] == s[right]:
                left -= 1
                right += 1
            return (right - left - 2) // 2
        right = -1
        j = -1
        arm_len = []
        end, start = -1, 0
        for i in range(m):
            if right >= i:
                i_sym = 2 * j - i
                min_arm = min(arm_len[i_sym], right -i )
                cur_arm = expend(i-min_arm, i+min_arm)
            else:
                cur_arm = expend(i, i)
            arm_len.append(cur_arm)
            if i + cur_arm > right:
                j = i
                right = i + cur_arm
            if 2 * cur_arm + 1 > end - start:
                start = i - cur_arm
                end = i + cur_arm
        return s[start+1:end+1:2]