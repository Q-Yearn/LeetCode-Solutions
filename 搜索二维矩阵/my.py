class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n-1]:
                left = 0
                right = n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                break
        return False


        