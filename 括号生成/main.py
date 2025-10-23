# 暴力DFS
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    result.append(A)
            else:
                generate(A+'(')
                generate(A+')')
        def valid(A):
            num = 0
            for c in A:
                if c == '(':
                    num += 1
                else:
                    num -= 1
                if num < 0:
                    break
            return num == 0
        generate("")
        return result


# 剪枝DFS
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def DFS(left, right, path):
            if len(path) == 2*n:
                result.append(path)
                return
            if left < n:
                DFS(left+1, right, path+'(')
            # 注意这里 不能没有左括号先有右括号
            # if right < n:
            if right < left:
                DFS(left, right+1, path+')')
        DFS(0, 0, "")
        return result


class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
