class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if i > 0 and nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                n -= 1
                continue
            i += 1
        return nums
