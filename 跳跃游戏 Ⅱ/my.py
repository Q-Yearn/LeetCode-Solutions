# DP
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        step = [float('inf')] * m
        step[0] = 0
        for i in range(0, m-1):
            for j in range(1, nums[i]+1):
                if i+j <= m-1:
                    step[i+j] = min(step[i+j], step[i]+1)
        return step[m-1]
