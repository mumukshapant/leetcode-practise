class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj= defaultdict(list)
        connected = defaultdict(set)
        depths = [0]*n
        cost = [0]*n

        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
            connected[u].add(v)
        
        def dfs(cur, par, inverted, depth): 
            res=0 
            for nei in adj[cur]: 
                if nei==par: 
                    continue
                if nei not in connected[cur]: 
                    res+= 1+dfs(nei, cur, inverted+1, depth+1)
                else: 
                    res+= dfs(nei, cur, inverted, depth+1)
            cost[cur] = inverted
           
            depths[cur] = depth
            
            return res 
        
        ans = [] 
        total  = dfs(0,-1,0,0)
        print(total)
        for i in range(n): 
            newcost = depths[i] - cost[i]
            cur = total - cost[i] + newcost
            ans.append(cur)
        return ans 