# 暴力求解  超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        length = len(nums)
        for i in range(1, length+1):
            for j in range(0,length):
                if j+i <= length:
                    if sum(nums[j:j+i]) == k:
                        ans += 1
        return ans
                
# 优化了一下  知道[j,i]子数组的和  那么就可以花费O(1)知道[j-1,i]子数组的和  不需要重新遍历了
# 但是还是很慢  会超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        length = len(nums)
        for i in range(length):
            j = i
            sums = 0
            while j >= 0:
                sums += nums[j]
                if sums == k:
                    ans += 1
                j -= 1
        return ans
                
        