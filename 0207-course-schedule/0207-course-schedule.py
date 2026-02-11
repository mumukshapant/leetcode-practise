class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = defaultdict(list)
        visited = set()

        for course,pre in prerequisites: 
            adj[course].append(pre)
        
        def dfs(course) :

            if course in visited: 
                return False
            
            if adj[course]== [] : 
                return True 
            
            visited.add(course)

            for p in adj[course]: 
                if dfs(p) ==False : 
                    return False
            
            visited.remove(course)
            adj[course]=[] # memoization -- to avoid repeated work. Eg  1 - [0,3]   2- [3,5]
            # We would explore 3 two times. 

            return True 
        
        for c in range(n): 
           if not dfs(c): 
                return False
        return True
