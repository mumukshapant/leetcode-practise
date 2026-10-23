class Solution(object):
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m,n= len(g), len(g[0])
        count=0 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(x,y): 
            g[x][y]='2' #visited 
            for dr,dc in directions: 
                nr,nc=dr+x,dc+y

                if 0<=nr<m and 0<=nc<n and g[nr][nc]!='2' and g[nr][nc]=="1": 
                    dfs(nr, nc)



        for i in range(m): 
            for j in range(n): 
                if g[i][j]=="1": 
                    dfs(i,j)
                    count+=1
        return count
        
