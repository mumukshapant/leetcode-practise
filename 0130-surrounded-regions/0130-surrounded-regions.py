class Solution(object):
    def solve(self, g):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(g)
        n=len(g[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(row, col): 
            if row>=m or row<0 or col>=n or col<0 or g[row][col]!="O": 
                return 
            
            g[row][col]= True

            # DFS in all 4 directions
            for dr, dc in directions:
                helper(row + dr, col + dc)

        # STEP 1 

        # Go to every boundary and check if there is any 0 on the boundary. 
        # IF there is a 0 on the boundary, we run DFS on that cell. 
        # Every 0 cell connected to the boundary 0 will be marked as True. 
        # We mark as True meaning these cells will not be converted to X 

        for i in range(m): 
            for j in range(n): 
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and g[i][j] == "O":
                    helper(i, j)


        # STEP 2 - convert all the cells except True as "X"
        for i in range(m): 
            for j in range(n): 
                if g[i][j]!=True: 
                    g[i][j]= "X"

        # STEP 3 - convert all the cells that are True to "O"
        for i in range(m): 
            for j in range(n): 
                if g[i][j]==True: 
                    g[i][j]= "O"


            
            
