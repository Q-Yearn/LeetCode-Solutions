class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        def DFS(cur, index):
            if cur == target:
                result.append(path[:])
                return
            if cur > target:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                DFS(cur+candidates[i], i)
                path.pop()
        DFS(0, 0)
        return result