# 只会产生一种分割
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def check(sub):
            return sub == sub[::-1]
        result = []
        path = []
        def DFS(cur, l):
            if cur + l > len(s):
                return
            if cur == len(s):
                result.append(path[:])
                return
            a = s[cur:cur+l]
            if check(a):
                path.append(a)
                DFS(cur+l, 1)
                path.pop()
            else:
                DFS(cur, l+1)
        DFS(0, 1)
        return result

# 换一下顺序即可
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def check(sub):
            return sub == sub[::-1]
        result = []
        path = []
        def DFS(cur, l):
            if cur == len(s):
                result.append(path[:])
                return
            if cur + l > len(s):
                return
            DFS(cur, l+1)
            a = s[cur:cur+l]
            if check(a):
                path.append(a)
                DFS(cur+l, 1)
                path.pop()
                
        DFS(0, 1)
        return result


        