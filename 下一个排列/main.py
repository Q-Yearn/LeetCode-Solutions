class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        # 创建新列表并反转 错误的
        # nums[i:].reverse()
        nums[i:] = reversed(nums[i:])
