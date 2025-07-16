# 不用排序就可以
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for str in strs:
            tmp = tuple(sorted(str))
            if tmp in result:
                result[tmp].append(str)
            else:
                result[tmp] = [str]
        return [result[index] for index in result] 