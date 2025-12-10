# 荷兰国旗法
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = 0
        n = len(nums) - 1
        i = 0
        while i <= n:
            if nums[i] == 0:
                nums[i], nums[m] = nums[m], nums[i]
                m += 1
            if nums[i] == 2:
                nums[i], nums[n] = nums[n], nums[i]
                n -= 1
                continue
            i += 1
        return nums

# 还可以计数排序