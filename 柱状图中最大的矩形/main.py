class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        m = len(heights)
        left, right = [0] * m, [0] * m
        stack = []
        for i in range(m):
            index = -1
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(m-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                index = stack.pop()
            right[i] = stack[-1] if stack else m
            stack.append(i)  

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(m)) if m >0 else 0
        return ans

