class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i + 1
            right = length - 1
            target = -nums[i]
            while(left < right):
                if (nums[left] + nums[right] == target):
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif (nums[left] + nums[right] < target):
                    left += 1
                else:
                    right -= 1
        return result

