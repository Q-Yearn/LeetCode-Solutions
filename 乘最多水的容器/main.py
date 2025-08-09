# 每次移动height小的那个  代表以他为边界的最大容量已经算完了  边界减一
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        volume = 0
        while left != right:
            volume = max(volume, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return volume

