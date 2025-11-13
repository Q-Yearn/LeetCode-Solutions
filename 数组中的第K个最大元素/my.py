# 计数排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = [0] * ((2*(10**4))+1)
        for num in nums:
            result[num+10**4] += 1
        for i in range(len(result)-1, -1, -1):
            if result[i] >= k:
                return i-10**4
            k -= result[i]