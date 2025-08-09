class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxest = nums[0]
        length = len(nums)
        for i in range(length):
            j = i
            current_max = 0
            while j >= 0:
                current_max += nums[j]
                maxest = max(maxest, current_max)
                j -= 1
        return maxest


        