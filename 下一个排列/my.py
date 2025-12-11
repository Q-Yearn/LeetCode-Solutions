# 寻找交换位置逻辑复杂 不需要else分支
# 错误的代码
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = len(nums) - 1
        while i > 0:
            if flag == 1:
                break
            if nums[i] > nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                flag = 1
                left, right = i, len(nums) - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                break
            else:
                for j in range(i-1, 0, -1):
                    if nums[j] > nums[j-1] and nums[i] > nums[j-1]:
                        nums[j-1], nums[i] = nums[i], nums[j-1]
                        flag = 1
                        left, right = j, len(nums) - 1
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        break
            i -= 1

        if flag == 0:
            nums.reverse()

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = len(nums) - 1
        while i > 0:
            if flag == 1:
                break
            if nums[i] > nums[i-1]:
                # i-1之后肯定是降序
                j = len(nums) - 1
                while nums[j] <= nums[i-1]:
                    j -= 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                flag = 1
                left, right = i, len(nums) - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                break
            i -= 1

        if flag == 0:
            nums.reverse()

