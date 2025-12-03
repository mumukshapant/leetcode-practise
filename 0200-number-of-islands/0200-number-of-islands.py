class Solution(object):
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m= len(g)
        n = len(g[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        count=0 

        def dfs(r, c): 
            if r>=m or c>=n or r<0 or c<0 or g[r][c]!="1": 
                return 
            g[r][c]="2" #visited 
            for d in directions: 
                newrow =d[0]+r
                newcol = d[1]+c 
                dfs(newrow, newcol)


        for i in range(m): 
            for j in range(n): 
                if g[i][j]=="1": 
                    dfs(i, j)
                    count+=1

        return count

