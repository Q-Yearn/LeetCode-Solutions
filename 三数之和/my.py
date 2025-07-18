# 不能使用集合去重 因为可能出现 -1 -1 2这样的组合  可以三重循环  然后去重 但是会超时
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        i = 0
        result = []
        for i in range(length-1):
            for j in range(i+1, length):
                complement = 0 - (nums[i] + nums[j])
                if complement in nums[j+1:length]:
                    result.append([nums[i], nums[j], complement])
            final = [tuple(sorted(sub_list)) for sub_list in result]
            final_set = set(final)
            result = list(final_set)
        return result