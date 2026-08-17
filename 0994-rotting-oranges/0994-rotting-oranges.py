class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        q=deque() 
        fresh=0
        time=0

        directions= [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2: # rotten 
                    q.append((i,j))
                elif grid[i][j]==1: #fresh 
                    fresh+=1 
                
        if fresh==0 : 
            return 0 
                    
        while q and fresh>0 :
            for _ in range(len(q)): 
                
                r,c = q.popleft()

                for dr , dc in directions: 
                    newrow, newcol = r+dr, c+dc 
                    if newrow>=m or newcol>=n or newrow < 0 or newcol<0 or grid[newrow][newcol]!=1 : 
                        continue 
                    
                    grid[newrow][newcol]= 2 # mark rotten 
                    q.append((newrow, newcol))

                    fresh-=1
            time+=1
        return time if fresh==0 else -1
            