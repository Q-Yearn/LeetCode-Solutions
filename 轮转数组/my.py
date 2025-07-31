class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法一：最笨的办法 循环k次 每次移动一位 空间确实是O(1)
        # 方法二：循环一次，直接计算出每个数字轮转后的位置
        length = len(nums)
        result = [0] * length
        for i in range(len(nums)):
            pos = (i + k) % length
            result[pos] = nums[i]
        for i in range(len(nums)):
            nums[i] = result[i]
        return nums
