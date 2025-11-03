# 两次二分查找
# 改进第一次查找的复杂逻辑
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        # 这个是错的
        # [1, 3]错误测试样例  
        # 因为mid总是偏向两者间小的坐标
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[left]:
        #         right = mid - 1
        #     else:
        #         left = mid
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        k = left
        low = k
        high = k-1 + n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid%n] == target:
                return mid%n
            elif nums[mid%n] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


