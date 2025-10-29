class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def midsearch(low, high):
            if low > high:
                return low
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                index = midsearch(mid+1, high)
            else:
                index = midsearch(low, mid-1)
            return index
        index = midsearch(0, len(nums)-1)
        return index