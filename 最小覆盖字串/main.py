# 因为左指针的移动减少了字串的遍历数量
# 注意记录最短长度
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        count1 = [0] * 52
        count2 = [0] * 52
        for c in t:
            if 'a' <= c <= 'z':
                count1[ord(c) - ord('a')] += 1
            if 'A' <= c <= 'Z':
                count1[ord(c) - ord('A') + 26] += 1
        l = 0
        L = -1
        min_len = float('inf')
        for i in range(length):
            if 'a' <= s[i] <= 'z':
                count2[ord(s[i]) - ord('a')] += 1
            if 'A' <= s[i] <= 'Z':
                count2[ord(s[i]) - ord('A') + 26] += 1
            r = i
            while all(x <= y for x, y in zip(count1, count2)) and l <= r:
                if r-l+1 < min_len:
                    min_len = r - l + 1
                    L = l
                if s[l] in t:
                    if 'a' <= s[l] <= 'z':
                        count2[ord(s[l]) - ord('a')] -= 1
                    if 'A' <= s[l] <= 'Z':
                        count2[ord(s[l]) - ord('A') + 26] -= 1
                l += 1
        return "" if L == -1 else s[L:L+min_len]

