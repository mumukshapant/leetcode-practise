class Solution(object):
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        
        adj = defaultdict(list)
        res=[]

        for course,p in prerequisites: 
            adj[course].append(p)
        cycle = set()
        visited = set()
        
        def dfs(course): 
            '''
            A course has 3 possible states : 
            - visited   : course has been added to output
            - visiting  : course not added to output, but added to cycle
            - unvisited : course not added to output, or cycle
            '''
        

            if course in cycle: 
                return False
            if course in visited: 
                return True
            cycle.add(course)

            for p in adj[course]: 
                if dfs(p)==False: 
                    return False
            # if course has no prerequistse, []
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        

        for c in range(n): 
            if dfs(c)==False: 
                return []
        return res