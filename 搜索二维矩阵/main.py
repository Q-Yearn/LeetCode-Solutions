# 两次二分查找
# O(logm + logn)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        left1 = 0
        right1 = m - 1
        row = 0
        while left1 <= right1:
            mid = (left1 + right1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left1 = mid + 1
            else:
                right1 = mid - 1
        row = right1
        left2 = 0
        right2 = n - 1
        while left2 <= right2:
            mid = (left2 + right2) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        return False


# 视为一维数组查找
# O(logm*n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



# 从左下角开始找
# O(m + n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        row = m - 1
        col = 0
        while row >= 0 and col <= n-1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False