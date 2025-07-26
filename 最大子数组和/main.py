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
from typing import List

class Status:
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum = lSum  # 左子段最大和
        self.rSum = rSum  # 右子段最大和
        self.mSum = mSum  # 最大子段和
        self.iSum = iSum  # 区间总和

class Solution:
    def pushUp(self, l: Status, r: Status) -> Status:
        iSum = l.iSum + r.iSum
        lSum = max(l.lSum, l.iSum + r.lSum)
        rSum = max(r.rSum, r.iSum + l.rSum)
        mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum)
        return Status(lSum, rSum, mSum, iSum)

    def get(self, a: List[int], l: int, r: int) -> Status:
        if l == r:
            return Status(a[l], a[l], a[l], a[l])
        m = (l + r) // 2
        lSub = self.get(a, l, m)
        rSub = self.get(a, m + 1, r)
        return self.pushUp(lSub, rSub)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.get(nums, 0, len(nums) - 1).mSum

