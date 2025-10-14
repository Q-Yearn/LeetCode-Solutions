# 必须搜索四个方向  不能只有右和下
# 因为可能出现这种情况
# 0 0 0
# 0 1 0
# 1 1 0
# DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        a = len(grid)
        b = len(grid[0])
        visited = [[0 for _ in range(b)] for _ in range(a)]

        def search(x, y):
            if visited[x][y] == 0:
                visited[x][y] = 1
                if x+1 < a and grid[x+1][y] == '1':
                    search(x+1, y)
                if x-1 > -1 and grid[x-1][y] == '1':
                    search(x-1, y) 
                if y+1 < b and grid[x][y+1] == '1':
                    search(x, y+1)
                if y-1 > -1 and grid[x][y-1] == '1':
                    search(x, y-1)

        num = 0
        for i in range(a):
            for j in range(b):
                if visited[i][j] == 0:
                    if grid[i][j] == '1':
                        num += 1
                        search(i, j)
        return num


# BFS
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        a = len(grid)
        b = len(grid[0])
        visited = [[0 for _ in range(b)] for _ in range(a)]

        def search(x, y):
            queue = deque([(x, y)])
            visited[x][y] = 1
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                nx, ny = queue.popleft()
                for dirx, diry in dirs:
                    curx = nx + dirx
                    cury = ny + diry
                    if curx >= 0 and curx < a and cury >= 0 and cury < b and visited[curx][cury] == 0 and grid[curx][cury] == '1':
                        visited[curx][cury] = 1
                        queue.append((curx, cury))

        num = 0
        for i in range(a):
            for j in range(b):
                if visited[i][j] == 0:
                    if grid[i][j] == '1':
                        num += 1
                        search(i, j)
        return num