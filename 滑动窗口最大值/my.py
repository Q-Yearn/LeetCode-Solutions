# 暴力法  超时 37/51
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            current_max = max(nums[i:i+k])
            result.append(current_max)
        return result

# 稍微优化了一下暴力法  但还是超时了  45/51
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_index, max_value = max(enumerate(nums[0:k]), key=lambda x: x[1])
        result.append(max_value)
        for i in range(1,len(nums)-k+1):
            if max_index != i-1:
                if max_value <= nums[i+k-1]:
                    max_value = nums[i+k-1]
                    max_index = i+k-1
            else:
                max_index, max_value = max(enumerate(nums[i:i+k]), key=lambda x: x[1])
                max_index = max_index + i
            result.append(max_value)
        return result
