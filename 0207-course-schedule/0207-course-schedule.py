class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj =defaultdict(list)
        for course, pre in prerequisites: 
            adj[course].append(pre)
        
        visited=set()

        def dfs(course): 
            if adj[course]==[] : # no prerequisite
                return True 
            if course in visited : 
                return False

            visited.add(course)

            for p in adj[course]: 
                if not dfs(p) : 
                    return False 
                
            visited.remove(course)
            adj[course]=[]
            return True 
        
        for c in range(n) : 
            if not dfs(c): 
                return False
        return True 

