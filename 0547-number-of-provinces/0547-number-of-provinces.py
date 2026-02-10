class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        visited = [False]*n
        count=0

        def dfs(node): 
            visited[node] = True 

            for nei in range(n): 
                if visited[nei]==False and isConnected[node][nei]: 
                    dfs(nei)
            
        

        for i in range(n): 
            if not visited[i]: 
                dfs(i)
                count+=1
        return count
    
    # Space = O(n) 
    # Time : O(n2)
            
