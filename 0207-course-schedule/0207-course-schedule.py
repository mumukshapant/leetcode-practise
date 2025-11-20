class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj = defaultdict(list) #defaultdict automatically creates a default value for any key 
        
        for course,pre in prerequisites: 
            adj[course].append(pre)
        
        visited=set()
        
        def dfs(course): 
            if course in visited: 
                return False
            
            if adj[course]==[]: #course can be taken, no pre requisite 
                return True 
            
            visited.add(course)
            for pre in adj[course]: 
                if not dfs(pre): #dfs returns False
                    return False 
            
            visited.remove(course)
            adj[course]=[]
            return True 

        for c in range(n): 
            if not dfs(c): 
                return False
        return True

        