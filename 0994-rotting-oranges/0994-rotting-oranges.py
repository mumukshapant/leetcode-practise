class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(g), len(g[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        q= deque()
        t,fresh=0,0

        for r in range(m): 
            for c in range(n): 
                if g[r][c]==2: #rotten orange
                    q.append((r,c))
                if g[r][c]==1: #fresh
                    fresh+=1

        while ((q) and (fresh>0)) : 
            for _ in range(len(q)):  # Time doesn’t pass per orange.Time passes per wave of infection.
            
                r,c = q.popleft()

                for dr,dc in directions: 
                    newrow= dr+r
                    newcol = dc+c

                    if newrow>=m or newcol>=n or newrow<0 or newcol<0 : 
                        continue 
                    if g[newrow][newcol]!=1: #not fresh
                        continue

                    g[newrow][newcol] = 2 #mark as rotten 
                    q.append((newrow, newcol))
                    fresh -=1 # fresh becomes rotten , so ofcourse fresh count is reduced
            t+=1
        return t if fresh==0 else -1
                
        