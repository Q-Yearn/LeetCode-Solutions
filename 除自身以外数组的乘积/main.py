# 直接用最后的返回数组储存前i-1元素乘积
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
        R = 1
        for i in range(length-1, -1, -1):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer