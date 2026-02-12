class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        
        logs.sort(key=lambda x : x[0])

        #adj = defaultdict(set)
        adj = [None] * n  # Use list instead of defaultdict for faster access
        
        for i in range(n): 
            # every one is aquainted with themself 
            adj[i] = {i}

        for t,a,b in logs: 
            if adj[a]==adj[b]: # This is to make it efficient, we don't have to check it again and again if adj of 2 nodes is same, eg 2 : {2,3, 4} and 4 : {2,3,4}
                continue

            union_set = adj[a].union(adj[b]) # using union because when a is connected to b, it means we get all friends of b also. 

            # Update ALL people in merged group to point to same set
            for person in union_set:
                adj[person] = union_set
        
        
        # Check if everyone is now connected
            if len(adj[a]) == n: # early termination, we can also use len(union_set)
                return t
        
        # Not everyone became connected
        return -1