class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c)-ord('a')] += 1
            tmp = tuple(count)
            if tmp not in result:
                result[tmp] = [str]
            else:
                result[tmp].append(str)
        return list(result.values())
        