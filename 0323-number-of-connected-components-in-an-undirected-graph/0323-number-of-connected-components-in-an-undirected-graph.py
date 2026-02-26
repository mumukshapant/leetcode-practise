class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        visited= [False]*n
        adj = defaultdict(list)
        count=0

        def dfs(node):

            visited[node]= True 
            for nei in adj[node]: 
                if not visited[nei]: 
                    dfs(nei)

        
        for u,v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(n): 
            if not visited[i]: 
                dfs(i)
                count+=1 
        
        return count
            
