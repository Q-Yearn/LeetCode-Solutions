# 二进制
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_max = 31
        ans = 0
        n = len(nums)
        while not ((n-1) >> bit_max):
            bit_max -= 1
        
        for bit in range(bit_max+1):
            # nums 中这一位为1的数量
            x = 0
            # 1 ... n-1 中这一位为1的数量
            y = 0
            for i in range(n):
                if nums[i] & (1 << bit):
                    x += 1
                if i >= 1 and i & (1 << bit):
                    y += 1
            if x > y:
                ans |= (1 << bit)
        return ans
    

# 快慢指针
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# 二分法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 1, n-1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for i in range(n):
                cnt += nums[i] <= mid
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans