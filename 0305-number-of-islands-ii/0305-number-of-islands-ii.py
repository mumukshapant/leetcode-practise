class Solution(object):
    def numIslands2(self, m, n, pos):
    
        '''
        For each point being added : 

        STEP 1 : Mark the cell as LAND       # grid[x][y] = 1
        

        STEP 2 : Create a new island for this cell        
        
            inside find((x, y))   
                --->  self.island += 1
        

        
        STEP 3 : Look in all 4 directions 
                (3.1)- check if neighboring cell is land or water
                - If neighbor is LAND, 
                       (3.1.1) - Find which island NEW CELL belongs to ( its root parent )
                       (3.1.2)  - Find which island the NEIGHBOR belongs to 

                       (3.1.3) - If NEW CELL and NEIGHBOR in same island : 
                            - Do nothing

                       (3.1.4)  - If NEW CELL and NEIGHBOR in different island : 
                            - Union() # Merge them 
                            - Decrement Island count by 1 
                        
        '''
        parents = {}
        self.island = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def find(a):

            if  a not in parents: 
                parents[a] = a # it has no parent, so parent of self 
                self.island +=1  # STEP 2: Create a new island for this cell
            
            # finding ultimate parent
            # while a !=parents[a] : 
            #     root = parents[a]

            while a != parents[a]:
                parents[a] = parents[parents[a]]  # Path compression optimization
                a = parents[a]

            return a 

        def union(a,b): 
            # STEP 3.1.1, 3.1.2 -- find which island NEW CELL & NEIGHBOR belongs to 
            a = find(a)
            b = find(b)

            if a==b :  # STEP (3.1.3)
                return 
            
            # STEP (3.1.4) If NEW CELL and NEIGHBOR in different islands: Merge them
            parents[a]=b 
            self.island-=1 




        g=[[0]*n for _ in range(m)]
        res=[]

        for x,y in pos : 
            g[x][y]= 1 # STEP 1 -- mark as island 
            find((x,y)) # STEP 2 --- creating a new island happens inside find()

            #STEP 3 - look in all directions 
            for dr,dc in directions: 
                r = dr+x
                c= dc+y

                # (3.1) check neighbor cell land or water 
                if r>=m or c>=n or r<0 or c<0 or g[r][c]==0 : 
                    continue 

                union((x,y),(r,c)) # if neighbor is land 

            res.append(self.island)
        return res




    
        