class Solution(object):
    def dfs(self, i, vis, path, graph):
        vis[i] = True
        path[i] = True
        for neigh in graph[i]:
            if not vis[neigh]: 
                if self.dfs(neigh, vis, path, graph): return True
            elif path[neigh]: return True

        path[i] = False

    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        vis = [False]*numCourses
        path = [False]*numCourses

        for i in range(numCourses):
            if not vis[i]:
                if self.dfs(i, vis, path, graph): return False

        return True
