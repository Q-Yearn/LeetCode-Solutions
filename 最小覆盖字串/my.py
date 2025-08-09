# 超时了 265/268
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        result = []
        count1 = [0] * 52
        for c in t:
            if 'a' <= c <= 'z':
                count1[ord(c) - ord('a')] += 1
            if 'A' <= c <= 'Z':
                count1[ord(c) - ord('A') + 26] += 1
        for i in range(length):
            j = i
            count2 = [0] * 52
            tmp = []
            while j >= 0:
                if 'a' <= s[j] <= 'z':
                    count2[ord(s[j]) - ord('a')] += 1
                if 'A' <= s[j] <= 'Z':
                    count2[ord(s[j]) - ord('A') + 26] += 1
                tmp.insert(0, s[j])
                if all(x <= y for x, y in zip(count1, count2)):
                    if len(result) == 0:
                        result = list(tmp)
                    else:
                        if len(result) > len(tmp):
                            result = list(tmp)
                    break 
                j -= 1
        return "".join(result)

