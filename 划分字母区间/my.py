class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        m = len(s)
        cur = 0
        index = s[::-1].index(s[cur])
        end = m - index - 1
        # 先找所有1个1个的划分
        while end == cur:
            res.append(1)
            cur += 1
            if cur >= m :
                break
            index = s[::-1].index(s[cur])
            end = m - index - 1 
        for i in range(cur + 1, m):
            index = s[::-1].index(s[i])
            end = max(end, m - index - 1)
            if i == end:
                res.append(end - cur + 1)
                if i < m - 1:
                    cur = end + 1
                    index = s[::-1].index(s[cur])
                    end = m - index - 1
        return res


# 使用rindex从右开始找
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        m = len(s)
        cur = 0
        index = s.rindex(s[cur])
        end = index
        while end == cur:
            res.append(1)
            cur += 1
            if cur >= m :
                break
            index = s.rindex(s[cur])
            end = index
        for i in range(cur + 1, m):
            index = s.rindex(s[i])
            end = max(end, index)
            if i == end:
                res.append(end - cur + 1)
                if i < m - 1:
                    cur = end + 1
                    index = s.rindex(s[cur])
                    end = index
        return res


# 因为在更新end  所以可以从0开始遍历了  不用先给end赋值
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        m = len(s)
        cur = 0
        end = 0
        for i in range(m):
            index = s.rindex(s[i])
            end = max(end, index)
            if i == end:
                res.append(end - cur + 1)
                cur = i + 1
        return res