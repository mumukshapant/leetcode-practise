class Solution(object):
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = defaultdict(list)
        for c, p in prerequisites: 
            adj[c].append(p)
        
        res=[]
        cycle = set()   # current path (cycle detection)
        visited = set()    # already processed

        def dfs(course): 
        
            if course in cycle: # cycle detected
                return False
            
            if course in visited: # already processed
                return True
             
            cycle.add(course)

            for pre in adj[course]: 
                if not dfs(pre): 
                    return False 

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True 
            
        for c in range(n): 
            if not dfs(c): 
                return [] 
        return res 