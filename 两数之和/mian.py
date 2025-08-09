class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in tmp:
                return [tmp[complement], index]
            else:
                tmp[num] = index
