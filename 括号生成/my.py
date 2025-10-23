# 这种情况下在添加左括号后只能添加一个右括号
# 没有考虑连续添加几个右括号的情况
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def DFS(left, right, path):
            if left <  n:
                left += 1
                path += '('
            if right == n:
                result.append(path)
                return
            for c in ['', ')']:
                if c == '':
                    if left < n:
                        DFS(left, right, path+c)
                    else:
                        continue
                else:
                    DFS(left, right+1, path+c)
        DFS(0, 0, "")
        return result
        