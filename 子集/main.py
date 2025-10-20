# DFS改进1
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        subset = []
        m = len(nums)
        def DFS(start):
            result.append(subset[:])
            for i in range(start, m):
                subset.append(nums[i])
                DFS(i+1)
                subset.pop()

        DFS(0)
        return result

# DFS改进2
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        subset = []
        m = len(nums)
        def DFS(start):
            if start == m:
                result.append(subset[:])
                return 
            subset.append(nums[start])
            DFS(start+1)
            subset.pop()
            DFS(start+1)

        DFS(0)
        return result

# 二进制迭代枚举
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        m = len(nums)
        for i in range(1 << m):
            path = []
            for j in range(m):
                if i & (1 << j):
                    path.append(nums[j])
            result.append(path)
        return result