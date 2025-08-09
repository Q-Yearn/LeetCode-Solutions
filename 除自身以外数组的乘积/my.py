class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0] * length
        pre = [0] * length
        suff = [0] * length
        for i in range(length):
            if i == 0:
                suff[i] = nums[i]
            else:    
                suff[i] = suff[i-1] * nums[i] 
        for i in range(length-1, -1, -1):
            if i == length-1:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i+1] * nums[i]
        for i in range(length):
            if i == 0:
                answer[i] = pre[i+1]
            elif i == length-1:
                answer[i] = suff[i-1]
            else:
                answer[i] = pre[i+1] * suff[i-1]
        return answer

        