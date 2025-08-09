# 暴力双层循环  超时了
class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                high = min(height[i], height[j])
                volume = max(volume, high * (j-i))
        return volume
