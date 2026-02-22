class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid :
            return 0 
        rows, col = len(grid), len(grid[0])

        count=0 
        
        def dfs(r,c) : 
            if r>=rows or c>=col or r<0 or c<0 or grid[r][c] !="1": 
                return
            
            grid[r][c]="0" # visited 
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows): 
            for c in range(col): 
                if grid[r][c]=="1" : 
                    count+=1
                    dfs(r,c)
        return count

             
            
            
              
