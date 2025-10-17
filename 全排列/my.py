class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        visited = [0] * length
        tmp = []
        def dfs(num):
            if num == length:
                # 不能这么写  这是一个引用后面会被修改
                # result.append(tmp)
                result.append(tmp[:])
                return
            for i in range(length):
                if visited[i] == 0:
                    tmp.append(nums[i])
                    visited[i] = 1
                    dfs(num+1)
                    tmp.pop()
                    visited[i] = 0
        dfs(0)
        return result
        