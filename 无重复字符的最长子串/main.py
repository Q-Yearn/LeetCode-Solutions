class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        result = []
        longest = 0
        right = -1
        for i in range(length):
            if i != 0:
                result.remove(s[i-1])
            while right+1 < length and s[right+1] not in result:
                result.append(s[right+1])
                right += 1
            longest = max(longest, len(result))
        return longest