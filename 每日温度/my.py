# 超时
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        m = len(temperatures)
        ans = [0] * m
        for i in range(m):
            day = 0
            for j in range(i+1, m):
                day += 1
                if temperatures[j] > temperatures[i]:
                    ans[i] = day
                    break
        return ans
