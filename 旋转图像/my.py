class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        loop_num = m // 2
        i = 0
        # 每次循环四个方向移动的元素数量 初始值
        shift_num = m - 1
        while i < loop_num:
            for j in range(shift_num):
                # 逆时针
                tmp = matrix[i][i+j]
                matrix[i][i+j] = matrix[m-i-1-j][i]
                matrix[m-i-1-j][i] = matrix[m-i-1][m-i-1-j]
                matrix[m-i-1][m-i-1-j] = matrix[i+j][m-i-1]
                matrix[i+j][m-i-1] = tmp
                # 顺时针
                # matrix[i][i+j] = matrix[i+j][m-i-1]
                # matrix[i+j][m-i-1] = matrix[m-i-1][m-i-1-j]
                # matrix[m-i-1][m-i-1-j] = matrix[m-i-1-j][i]
                # matrix[m-i-1-j][i] = tmp
            shift_num -= 2
            i += 1
        