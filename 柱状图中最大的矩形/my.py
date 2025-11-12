# 超时
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        m = len(heights)
        max_mat = [x for x in heights]
        for i in range(m):
            mat = max_mat[i]
            for j in range(i+1, m):
                mat = min(mat, heights[j])
                max_mat[i] = max(max_mat[i], mat*(j-i+1))
        return max(max_mat)


# 以高开始暴力枚举 向两边扩展  
# 遇到小于当前高的就停止  剩余情况会在小于的那个高为当前高时包含
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        m = len(heights)
        max_mat = 0
        for i in range(m):
            height = heights[i]
            left, right = i, i
            while left - 1 >= 0 and heights[left-1] >= height:
                left -= 1
            while right + 1 < m and heights[right+1] >= height:
                right += 1
            max_mat = max(max_mat, height*(right-left+1))
        return max_mat

