class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            new_res = []
            for sub in result:
                for i in range(len(sub)+1):
                    new_sub = sub[:i] + [num] + sub[i:]
                    new_res.append(new_sub)
            result = new_res
        return result
        