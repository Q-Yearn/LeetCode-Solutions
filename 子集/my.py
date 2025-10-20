class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        m = len(nums)
        def DFS(start, length, path):
            if m - start < length - len(path):
                return
            if len(path) == length:
                result.append(path[:])
            for i in range(start, m):
                path.append(nums[i])
                DFS(i+1, length, path)
                path.pop()

        # 子集长度
        for i in range(1, m+1):
            DFS(0, i, [])
        result.insert(0, [])
        return result