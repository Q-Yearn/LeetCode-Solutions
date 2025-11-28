class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        imax = nums[0]
        imin = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            if curr < 0:
                imax, imin = imin, imax
            
            imax = max(curr, imax * curr)
            imin = min(curr, imin * curr)
            
            res = max(res, imax)
            
        return res