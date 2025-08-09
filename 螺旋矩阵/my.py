# 比较难想  注意循环次数  和  从右到左和从下到上遍历的条件
# 主要是i这个东西比较难以理解 其实同时代表了 左和上的变化 m-i和n-1代表了 下和右的变化 
# 可以定义上下左右四个点  循环结束用左小于等于右同时上小于等于下(这个其实就等于m,n最小值减1除以2那一步)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        row = (min(m,n) - 1) // 2
        i = 0
        while i <= row:
            for j in range(i, n-i):
                result.append(matrix[i][j])
            for j in range(i+1, m-i):
                result.append(matrix[j][n-i-1])
            if m-i-1 > i:
                for j in range(n-i-2, i-1, -1):
                    result.append(matrix[m-i-1][j])
            if i < n-i-1:
                for j in range(m-i-2, i, -1):
                    result.append(matrix[j][i])
            i += 1
        return result

