class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        def check(sub):
            for i in range(len(sub) // 2):
                if sub[i] != sub[len(sub)-1-i]:
                    return False
            return True
        result = []
        path = []
        def DFS(cur):
            if cur == l:
                result.append(path[:])
                return
            for i in range(cur+1, l+1):
                a = s[cur:i]
                if check(a):
                    path.append(a)
                    DFS(i)
                    path.pop()
        DFS(0)
        return result

# 动态规划
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        f = [[True for _ in range(l)] for _ in range(l)]
        for i in range(l-1,-1,-1):
            for j in range(i+1, l):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
        
        result = []
        ans = []
        def dfs(a):
            if a==l:
                result.append(ans[:])
                return
            for i in range(a, l):
                if f[a][i]:
                    ans.append(s[a:i+1])
                    dfs(i+1)
                    ans.pop()
        
        dfs(0)
        return result
        