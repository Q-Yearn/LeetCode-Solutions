# 贪心算法
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        end = 0
        far = 0
        step = 0
        for i in range(m-1):
            far = max(far, i+nums[i])
            if i == end:
                step += 1
                end = far
        return step
