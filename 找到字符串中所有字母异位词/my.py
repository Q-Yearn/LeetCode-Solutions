# # 太慢  切片太慢了 而且不用每次都重新计算字符频率统计  只需要维护一个就够了
# class Solution:
#     def compare(self, str1, str2) -> bool:
#         tmp1 = [0] * 26
#         tmp2 = [0] * 26
#         for c in str1:
#             tmp1[ord(c) - ord('a')] += 1
#         for c in str2:
#             tmp2[ord(c) - ord('a')] += 1
#         return tmp1 == tmp2
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         length1 = len(s)
#         length2 = len(p)
#         result = []
#         if length1 < length2:
#             return []
#         for i in range(length1-length2+1):
#             tmp = s[i:i+length2]
#             if self.compare(tmp, p):
#                 result.append(i)
#         return result

# 优化后
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length1 = len(s)
        length2 = len(p)
        if length1 < length2:
            return []
        tmp1 = [0] * 26
        tmp2 = [0] * 26
        result = []
        for i in range(length2):
            tmp1[ord(s[i]) - ord('a')] += 1
            tmp2[ord(p[i]) - ord('a')] += 1
        if tmp1 == tmp2:
            result.append(0)
        for i in range(length1 - length2):
            tmp1[ord(s[i]) - ord('a')] -= 1
            tmp1[ord(s[i + length2]) - ord('a')] += 1
            if tmp1 == tmp2:
                result.append(i+1) 
        return result
