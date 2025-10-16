# DFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        self.valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(node):
            visited[node] = 1
            for a in edges[node]:
                if visited[a] == 0:
                    dfs(a)
                    # 加这句避免冗余u
                    if not self.valid:
                        return
                elif visited[a] == 1:
                    self.valid = False
                    return
            visited[node] = 2
        
        for i in range(numCourses):
            if self.valid and not visited[i]:
                dfs(i)
        return self.valid


# BFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)
        inedg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            inedg[info[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if inedg[u] == 0])
        visit = 0

        while q:
            u = q.popleft()
            for v in edges[u]:
                inedg[v] -= 1
                if inedg[v] == 0:
                    q.append(v)
            visit += 1

        return visit == numCourses
