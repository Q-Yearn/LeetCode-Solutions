from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        def check():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return False
            return True

        def neighbor(x, y):
            for c, d in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= c < m and 0 <= d < n:
                    yield c, d

        min = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            x, y, min = queue.popleft()
            for a, b in neighbor(x, y):
                if grid[a][b] == 1:
                    grid[a][b] = 2
                    queue.append((a, b, min+1))
        
        # 等价于if any(1 in row for row in grid):
        if not check():
            return -1

        return min
            
