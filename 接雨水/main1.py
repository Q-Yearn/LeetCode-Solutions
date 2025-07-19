# 优化的双指针
# 相同时同时处理左右  需要注意left可以等于right
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        ans = 0
        while(left <= right):
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if leftmax < rightmax:
                ans += leftmax - height[left]
                left += 1
            elif leftmax > rightmax:
                ans += rightmax - height[right]
                right -= 1
            else:
                ans += leftmax - height[left]
                if left < right:
                    ans += rightmax - height[right]
                left += 1
                right -= 1
        return ans

# 只处理一侧
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        ans = 0
        while(left < right):
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if leftmax < rightmax:
                ans += leftmax - height[left]
                left += 1
            else:
                ans += rightmax - height[right]
                right -= 1
        return ans


