class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        if m < 2:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        mem = {}
        def dfs(cur, index):
            if cur == target:
                return True
            if index >= m:
                return False
            if cur > target:
                return False
            state = (cur, index)
            if state in mem:
                return mem[state]
            res = dfs(cur, index+1) or dfs(cur+nums[index], index+1)
            mem[state] = res
            return res
        return dfs(0, 0)
                

        