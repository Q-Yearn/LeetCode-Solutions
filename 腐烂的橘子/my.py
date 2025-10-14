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
        min = 0
        def check():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return False
            return True
        
        while True:
            queue = []
            if check():
                break
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                                # 不能直接在这修改为2  必须先记录一整轮结束后再腐蚀
                                queue.append((x, y))
            # 因为记录了是否有腐蚀的  恰好可以利用这个判断是否有永远不能被腐蚀的
            if not queue:
                return -1
            while queue:
                c, d = queue.pop()
                grid[c][d] = 2
            min += 1
        return min
            
