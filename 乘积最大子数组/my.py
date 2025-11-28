class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1, 1] for _ in range(len(nums))]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            pre_max = dp[i-1][0]
            pre_min = dp[i-1][1]

            dp[i][0] = max(nums[i], nums[i]*pre_max, nums[i]*pre_min)
            dp[i][1] = min(nums[i], nums[i]*pre_max, nums[i]*pre_min)

            res = max(res, dp[i][0])
        return res


