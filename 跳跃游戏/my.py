# 怎么剪枝  都会超内存
# 无法避免一次一步的深度递归
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.flag = False
        self.visited = [0] * len(nums)
        def jump(index):
            if index == len(nums)-1:
                self.flag = True
                return
            for i in range(1, nums[index]+1):
                if self.flag == True:
                    break
                if index + i == len(nums) - 1:
                    self.flag = True
                    break 
                if index + i < len(nums)-1  and self.visited[index+i] == 0 and nums[index+i] != 0: 
                    self.visited[index+i] =1
                    jump(index+i)
        jump(0)
        return self.flag
        