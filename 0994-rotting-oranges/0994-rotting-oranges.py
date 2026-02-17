class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        t=0 
        m,n=len(g),len(g[0])
        q=deque()
        fresh=0


        for r in range(m): 
            for c in range(n): 
                if g[r][c]==2 : #rotten 
                    q.append((r,c))
                elif g[r][c]==1: 
                    fresh+=1
        
        if fresh==0 :
            return 0 
        
    
        while q and fresh>0 : 
            for _ in range(len(q)): 
                r,c = q.popleft()
                for dr, dc in directions: 
                    newrow= dr+r
                    newcol= dc+c 

                    if newrow>=m or newcol>=n or newrow < 0 or newcol<0 or g[newrow][newcol]!=1 : 
                        continue 
                    
                    g[newrow][newcol]=2 #mark rotten 
                    q.append((newrow, newcol))

                    fresh-=1 
            t+=1

    
        return t if fresh == 0 else -1

                


        


            
        