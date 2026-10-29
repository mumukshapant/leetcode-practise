class Solution(object):
    def validPath(self, n, edges, s, d):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if s==d: 
            return True 
        adj=defaultdict(list)
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        vis=set()
        def dfs(node): 
            if node==d: 
                return True 
            vis.add(node)
            for nei in adj[node]: 
                if nei not in vis: 
                    if dfs(nei):
                        return True 
            return False

        return dfs(s)



        