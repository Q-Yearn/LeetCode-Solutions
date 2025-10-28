class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        pos = set()
        def judge(i, j):
            tmp = set()
            for x,y in pos:
                tmp.add((i, y))
                # 不需要判断是否越界了
                tmp.add((i, y+(i-x)))
                tmp.add((i, y-(i-x)))
            if (i, j) not in tmp:
                return True
            return False
        
        def dfs(i):
            if i == n:
                result.append([])
                for x in range(n):
                    result[-1].append("")
                    for y in range(n):
                        if (x,y) in pos:
                            result[-1][x] += 'Q'
                        else:
                            result[-1][x] += '.'
            for j in range(n):
                if judge(i, j):
                    pos.add((i, j))
                    dfs(i+1)
                    pos.remove((i, j))
        dfs(0)
        return result
