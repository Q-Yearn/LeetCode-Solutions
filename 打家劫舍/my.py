# 这里的dp代表偷窃当前房屋能获得的最大金额
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0], nums[1])
        if m == 3:
            return max(nums[0]+nums[2], nums[1])
        nums[2] += nums[0]
        for i in range(3, m):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[m-1], nums[m-2])