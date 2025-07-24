# 之前的方法还可以在优化一下  使用优先队列保持最大值  不用每次都得切片然后求解 其余思路一直  都是考虑前一次的最大值是否还在滑动窗口里
# 进一步优化优先队列  可以在滑动窗口移动时  如果队尾的元素小直接出队
# 别的方法  分组
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        for i in range(n):
            if i%k == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = max(prefix[i-1], nums[i])
        for i in range(n-1,-1,-1):
            if i == n-1 or (i+1)%k ==0:
                suffix[i] = nums[i]
            else:
                suffix[i] = max(suffix[i+1], nums[i])
        result = [max(prefix[i+k-1], suffix[i]) for i in range (n-k+1)] 
        return result   