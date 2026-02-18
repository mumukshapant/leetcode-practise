class Solution(object):
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m,n = len(g), len(g[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        count=0 

        def dfs(r,c): 
            if r>=m or c>=n or r<0 or c<0 or g[r][c]!="1" : 
                return 0
            
            g[r][c] = "2" # visited
            for dr, dc in directions: 
                newrow , newcol = dr+r , dc+c 
                dfs(newrow, newcol)
            
            return count 
                

        for i in range(m): 
            for j in range(n):
                if g[i][j]=="1":  
                    dfs(i, j)
                    count+=1
        return count