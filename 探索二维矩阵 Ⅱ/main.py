# 每行使用二分查找  也可以python自带的函数bisect.bisect_left()>=或者bisect.bisect_right(>)
class Solution(object):
    def mid_search(self, row, target):
        low = 0
        high = len(row) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            if row[mid] == target:
                return mid
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            index = self.mid_search(row, target)
            if index >= 0:
                return True
        return False

# z字形查找 看子矩阵右上角元素  如果大于target 这一列都大于  列减1  如果小于target这一行都小于  行加1
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = n - 1
        while x < m and y >= 0 :
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

    