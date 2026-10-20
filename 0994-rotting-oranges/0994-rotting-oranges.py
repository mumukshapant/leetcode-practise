class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(g), len(g[0])
        q=deque() 
        fresh=0 

        #0- empty 
        #1- fresh 
        #2- rotten 

        for i in range(m): 
            for j in range(n): 
                if g[i][j]==2: 
                    q.append([i,j])
                elif g[i][j]==1:
                    fresh+=1
        t=0

        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0 : 
            t+=1
            for _ in range(len(q)):
                 
                r,c= q.popleft()
                for dr,dc in directions: 
                    newrow, newcol = r+dr, c+dc

                    if 0<=newrow<m and 0<=newcol<n and g[newrow][newcol]==1:
                        q.append([newrow, newcol])
                        g[newrow][newcol]=2
                        fresh-=1
        return -1 if fresh>0 else t



            