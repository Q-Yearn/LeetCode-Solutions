# 贪心算法不合适  
# 因为就算开始依次以每个平方数开始减，后面仍可能是从次大的开始
# 要考虑每种情况可以考虑深搜和广搜这种
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = float('inf')
        m = int(math.sqrt(n))
        for i in range(m, 0, -1):
            tmp = n
            cur = i
            cnt = 0
            while True:
                if cur < 1 or tmp <= 0:
                    break
                if tmp >= cur ** 2:
                    tmp -= cur ** 2
                    cnt += 1
                else:
                    cur -= 1
            if tmp == 0:
                res = min(res, cnt)
        return res


# 深搜
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = float('inf')
        def DFS(cur, tmp, cnt):
            # 加入剪枝条，不然会超时
            if cnt >= self.res:
                return
            if tmp == 0:
                # 加入剪枝条后这一步就不用比较了
                # self.res = min(self.res, cnt)
                self.res = cnt
                return
            # 这一步没必要加  因为循环里的所有判断保证不会到这
            # if cur < 1 or tmp <=0:
            #     return
            for i in range(cur, 0, -1):
                if tmp >= i ** 2:
                    DFS(i, tmp - i**2, cnt+1)
                else:
                    continue
        cur = int(math.sqrt(n))
        DFS(cur, n, 0)
        return self.res
    

# 深搜
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义为集合  因为可以去重
        queue = {n}
        level = 0
        while queue:
        # 也可以只是用一个队列 每次循环开始  使用size记录当前层的数量 但是这样就不能去重了
        # 列表只能当栈 pop  列表是collections.deque popleft
            level += 1
            new_queue = set()
            for num in queue:
                i = 1
                while i * i <= num:
                    tmp = num - i*i
                    if tmp == 0:
                        return level
                    new_queue.add(num - i*i)
                    i += 1
            queue = new_queue