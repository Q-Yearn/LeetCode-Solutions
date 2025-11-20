# 没必要每次找
# 直接一次循环找出每个字符的最后位置
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        cur = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                res.append(end - cur + 1)
                cur = i + 1
        return res