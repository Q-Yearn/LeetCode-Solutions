class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        self.flag = False
        visited = [[0 for _ in range(n)] for _ in range(m)]
        def DFS(i, j, k):
            if self.flag == True:
                return
            if k == len(word):
                self.flag = True
                return
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                    if board[x][y] == word[k]:
                        visited[x][y] = 1
                        DFS(x, y, k+1)
                        visited[x][y] = 0
                
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited[i][j] = 1
                    DFS(i, j, 1) 
                    visited[i][j] = 0
                    if self.flag == True:
                        return self.flag
        return False