class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = {}
        ans = 0
        pre = 0
        pre_sum[0] = 1
        for i in nums:
            pre += i
            if pre - k in pre_sum:
                ans += pre_sum[pre - k]
            if pre not in pre_sum:
                pre_sum[pre] = 1
            else:
                pre_sum[pre] += 1
        return ans
                
        