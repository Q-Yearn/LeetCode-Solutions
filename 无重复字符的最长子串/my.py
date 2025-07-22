# 比官方题解优化了点
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        longest = 0
        for c in s:
            if c in result:
                result = result[result.index(c)+1:]
            result.append(c)
            longest = max(longest, len(result))
        return longest
