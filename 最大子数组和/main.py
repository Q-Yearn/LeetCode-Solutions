# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxest = nums[0]
        length = len(nums)
        pre = 0
        for i in range(length):
            pre = max(pre+nums[i], nums[i])
            maxest = max(pre, maxest)
        return maxest

# 分治
class Status:
    def __init__(self, lsum, rsum, msum, isum):
        self.lsum = lsum
        self.rsum = rsum
        self.msum = msum
        self.isum = isum

class Solution(object):
    def merge(self, l, r):
        isum = l.isum + r.isum
        lsum = max(l.lsum, l.isum + r.lsum)
        rsum = max(r.rsum, r.isum + l.rsum)
        msum = max(max(l.msum, r.msum), l.rsum + r.lsum)  # ← 关键修正
        return Status(lsum, rsum, msum, isum)

    def get(self, nums, l, r):
        if l == r:
            return Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) // 2
        lstatus = self.get(nums, l, m)
        rstatus = self.get(nums, m + 1, r)
        return self.merge(lstatus, rstatus)

    def maxSubArray(self, nums):
        return self.get(nums, 0, len(nums) - 1).msum

