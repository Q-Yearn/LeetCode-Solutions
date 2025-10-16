# 仿照链表检查环的思路
# 在这里不适用  因为这里是多对多的关系  不是一对一  
# for x, y in prerequisites:
#   rela[y] = x
# 当一门课是多门课的前置课程时 前后关系会被后续覆盖掉
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        rela = {}
        for x, y in prerequisites:
            rela[y] = x
        for i in range(numCourses):
            tmp = set()
            if i in rela:
                a = i
                while a in rela:
                    tmp.add(a)
                    a = rela[a]
                    if a in tmp:
                        return False
        return True
