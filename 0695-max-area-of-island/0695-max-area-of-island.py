class Solution(object):
    def maxAreaOfIsland(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m,n = len(g), len(g[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
    
        maxarea= 0

        def dfs(r,c): 
            
            if r>=m or c>=n or r<0 or c<0 or g[r][c]!=1 : 
                return 0
            
            area=1
            g[r][c] = 2 # visited

            for dr, dc in directions: 
                newrow , newcol = dr+r , dc+c 
                area+=dfs(newrow, newcol)
                
            return area
        
        for i in range(m): 
            for j in range(n):
                if g[i][j]==1:  
                    maxarea= max( dfs(i, j), maxarea)
                    
        return maxarea