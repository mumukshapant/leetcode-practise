class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        visit = [False] * n
        count = 0

        def dfs(node):
            visit[node] = True
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    dfs(neighbor)

        # EOF 
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1  # each unvisited node starts a new component

        return count