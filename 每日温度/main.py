# 暴力法
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        m = len(temperatures)
        ans = [0] * m
        nxt = dict()
        big = 10**9
        for i in range(m-1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(temperatures[i]+1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans


# 单调栈
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        m = len(temperatures)
        stack = []
        ans = [0] * m
        for i in range(m):
            cur = temperatures[i]
            while stack and temperatures[stack[-1]] < cur:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
