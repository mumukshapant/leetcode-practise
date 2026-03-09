class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        oggraph  = defaultdict(set)


        for u,v in edges: 
            adj[u].append(v)
            adj[v].append(u)

            oggraph[u].add(v)
        
        cost=[0]*n # number of edges that had to be reversed
        depths=[0]*n # distance (no. of edges) from node 0 to node i

        def dfs(curr, par, inverted, depth): 
            res=0 
            for nei in adj[curr]: 
                if nei==par: 
                    continue 
                if nei not in oggraph[curr]: # no real edge exists, so inverted ++ 
                    # so cost A will be increased 
                    res += 1+ dfs(nei, curr, inverted+1, depth+1)
                else: 
                    res += dfs(nei, curr, inverted, depth +1 )
            cost[curr] = inverted 
            depths[curr] = depth 
            return res 

        ans = [] 
        total = dfs(0,-1,0,0)  # total = minimum reversals to make every node rechable needed if root = 0

        for i in range(n): 
            curr = total + depths[i] - 2*cost[i] 
            ans.append(curr)
        return ans 

    

'''
Step 1: 
    Solve the problem for node 0 (pick any root).

Step 2: 
    Derive the answer for every other node in O(1) using the relationship between parent and child answers. This is Re Rooting 


-- Why are we chosing starting node as 0, root could be any one? 
Because This graph is a Tree ( given ). 
-> Tree has a property "Between any two nodes there is exactly one path"
-> Because of that, if we compute the reversal cost for one root, we can derive the cost for all other roots
-> Suppose we want root = i.

    Only edges on the path from old root (0) → new root (i) change  direction relative to the root.

    All other edges stay the same.

    So we don’t need to recompute the entire tree — we just adjust the reversals along that path.



    when root was 0, these edges were pointing the wrong way, so we reversed them.
If root becomes i, they no longer need reversal.
So we subtract these from total:
total - cost[i]

'''