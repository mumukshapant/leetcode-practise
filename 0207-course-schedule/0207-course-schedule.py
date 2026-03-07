class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)

        for c,p in prerequisites: 
            adj[c].append(p)
        
        visited = [False]*n

        def dfs(course): 
            if adj[course]==[] : # no prerequisite
                return True 
            
            if course in visited : 
                return False 
            
            visited.append(course)

            for pre in adj[course]:
                if not dfs(pre ) :
                    return False     
        
            visited[course]= False 
            adj[course]= []
            return True 

        for c in range(n): 
            if not dfs(c):
                return False 
        return True 

        