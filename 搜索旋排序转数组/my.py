class Solution(object):
    # 可以过
    # 但是逻辑复杂  可能在搜索k时出现问题 
    # 测试样例可能检查不出错误  但是也可能是对的
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        k = 0
        while left <= right:
            mid = (left + right) // 2
            if mid-1 >= 0:
                if mid+1 < n:
                    if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                        # 下标加1
                        k = mid + 1
                        break  
                    if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                        k = mid
                        break
                else:
                    if nums[mid-1] > nums[mid]:
                        k = mid
                        break
            else:
                if mid+1 < n:
                    if nums[mid] > nums[mid+1]:
                        k = mid+1
                        break
                else:
                    # 就是只有一个数字的时候
                    k = 0
            # 和固定位置的比较  更鲁棒
            if nums[mid] < nums[0]:
            # if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        
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
