class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = len(nums)
        left = 0
        right = m - 1
        len1 = 0
        len2 = 0
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        tmp = index - 1
        while tmp >= 0:
            if nums[tmp] == target:
                len1 += 1
                tmp -= 1
            else:
                break
        tmp = index + 1
        while tmp <= m - 1:
            if nums[tmp] == target:
                len2 += 1
                tmp += 1
            else:
                break
        return [index-len1, index+len2]
        