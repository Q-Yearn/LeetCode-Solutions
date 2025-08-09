class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        matrix_new = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                matrix_new[j][m-1-i] = matrix[i][j]
        # 不能写成
        # matrix = matrix_new
        matrix[:] = matrix_new

# 矩阵逆时针旋转等于  先水平翻转然后转置
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for i in range(m//2):
            for j in range(m):
                matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 矩阵顺时针旋转等于  先转置然后水平翻转
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(m//2):
            for j in range(m):
                matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]

