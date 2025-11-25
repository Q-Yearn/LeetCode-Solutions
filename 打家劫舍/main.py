# 这里的dp前i+1个房屋最多能偷多少
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = len(nums)
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0], nums[1])
        res = [0] * m
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, m):
            res[i] = max(res[i-1], res[i-2]+nums[i])
        return res[m-1]