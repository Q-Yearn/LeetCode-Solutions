# 单调栈   你可以在等于小于时都入栈  会有一些不必要的计算
# 如果你想去掉这些不必要的计算  你需要在等于时  入栈最后一个相同高度的下标才是正确的(先出栈后入栈) 因为你需要根据最后一个相同数字的下标算正确的宽度
class Solution: 
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                high = min(height[stack[-1]], height[i]) - height[top]
                ans += width * high
            if stack and height[stack[-1]] == height[i]:
                stack.pop()
            stack.append(i)
        return ans
                