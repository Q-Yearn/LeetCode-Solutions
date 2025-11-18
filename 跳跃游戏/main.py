# 贪心算法
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        most = 0
        for i in range(len(nums)):
            if i <= most:
                most = max(most, i+nums[i])
                if most >= len(nums) - 1:
                    return True
        return False
        