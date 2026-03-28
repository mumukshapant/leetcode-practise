class Solution(object):
    def numIslands2(self, m, n, pos):

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        self.island=0 

        parents={} 

    
        def find(a): 
            if a not in parents: 
                parents[a] = a 
                self.island+=1
            
            while a!=parents[a]: 
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a 
        
        def union(a,b): # merge 2 islands 
            a = find(a)
            b = find(b)

            if a==b : 
                return 
            
            parents[a] = b # 
            self.island -=1 
        
        g=[[0]*n for _ in range(m)]
        res=[]

        for a,b in pos :
            g[a][b] = 1 # mark as island 
            find((a,b))

            for dx,dy in directions : 
                r = dx+a 
                c = dy+b

                # neighbor is water
                if r>=m or c>=n or r<0 or c<0 or g[r][c]==0 : 
                    continue 
                
                union(   (a,b), (r,c)  ) # neighbor is WATER 
            
            res.append(self.island)
        return res 

