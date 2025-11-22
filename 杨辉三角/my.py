class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 没必要先遍历一遍生成
        res = [[1]*i for i in range(1, numRows+1)]
        if numRows > 2:
            for i in range(2, numRows):
                for j in range(1, i):
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res