# 使用差值  需要考虑清楚  count中的数绝对值大于1的时候
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length1 = len(s)
        length2 = len(p)
        if length1 < length2:
            return []
        count = [0] * 26
        result = []
        for i in range(length2):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(p[i]) - ord('a')] -= 1
        differ = [c != 0 for c in count].count(True)
        if differ == 0:
            result.append(0)
        for i in range(length1 - length2):
            if count[ord(s[i]) - ord('a')] == 1:
                differ -= 1
            elif count[ord(s[i]) - ord('a')] == 0:
                differ += 1
            count[ord(s[i]) - ord('a')] -= 1

            if count[ord(s[i + length2]) - ord('a')] == -1: 
                differ -= 1
            elif count[ord(s[i + length2]) - ord('a')] == 0: 
                differ += 1
            count[ord(s[i + length2]) - ord('a')] += 1
            
            if differ == 0:
                result.append(i + 1)
        return result

