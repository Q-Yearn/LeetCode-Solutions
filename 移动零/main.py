class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while i < len(nums)-1:
            if nums[i] == 0:
                while nums[j] == 0:
                    j += 1
                    if j >= len(nums):
                        return nums
                nums[i] = nums[j]
                nums[j] = 0
            i += 1
            j += 1
            if j >= len(nums):
                return nums
        return nums