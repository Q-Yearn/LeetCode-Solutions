class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        visited = [[False]*n for _ in range(m)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dirindex = 0
        row = 0
        col = 0
        for i in range(total):
            result.append(matrix[row][col])
            visited[row][col] = True
            nextrow, nextcol = row + direction[dirindex][0], col + direction[dirindex][1]
            if not (0 <= nextrow < m and 0 <= nextcol < n and not visited[nextrow][nextcol]):
                dirindex = (dirindex + 1) % 4
            row += direction[dirindex][0]
            col += direction[dirindex][1]
        return result      
