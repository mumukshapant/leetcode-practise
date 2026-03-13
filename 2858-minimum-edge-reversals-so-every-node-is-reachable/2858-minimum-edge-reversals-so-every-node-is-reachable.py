class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        adj= defaultdict(list)
        og_graph = defaultdict(set)

        for u,v in edges: 
            adj[u].append(v)
            adj[v].append(u)

            og_graph[u].add(v)

        cost=[0]*n # min cost to reverse the edge so that every node is rechable
        depths= [0]*n # distance (no of edges) from node 0 to node i 

        def dfs(curr, par, inv, depth): 
            res =0 
            for nei in adj[curr]: 
                if nei==par: 
                    continue 
                
                if nei not in og_graph[curr]:  # no real edge exists 
                    res+=1+dfs(nei, curr, inv+1, depth+1)
                else: 
                    res+= dfs(nei, curr, inv, depth+1)

            cost[curr]=inv
            depths[curr]=depth
            return res     


        total_cost = dfs(0,-1, 0, 0 ) # assuming source is node 0 
        # For any other node, re rooting is done -- Only edges on the path from old root (0) → new root (i) change  direction relative to the root. 
        # So we do not have to RECOMPUTE the tree, We just adjust the values 

        ans=[]

        for i in range(n): 
            final_cost = (total_cost- cost[i]) + (depths[i] - cost[i])
            ans.append(final_cost) 
        
        return ans 
