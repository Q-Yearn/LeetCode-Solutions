# 思路是对的  但是多遍了一些东西  当你第一次遍历到非零时  下一次遍历从这开始就好  不用从处理好序列的下一个开始
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                j = i + 1
                while nums[j] == 0:
                    j += 1
                    if j >= len(nums):
                        return nums
                nums[i] = nums[j]
                nums[j] = 0
            i += 1
        return nums