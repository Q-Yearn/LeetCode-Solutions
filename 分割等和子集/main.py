# BFS
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
        tmp = {0}
        for num in nums:
            new_set = set()
            # 同时遍历和修改集合和字典会报错
            for s in tmp:
                if s+num == target:
                    return True
                if s+num < target:
                    new_set.add(s+num)
            tmp.update(new_set)
        return False


# dp
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
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target]



        
        