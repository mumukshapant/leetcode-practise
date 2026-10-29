class Solution(object):
    def islandPerimeter(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n= len(g), len(g[0])
        p=0 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(m): 
            for c in range(n): 
                if g[r][c] ==1: # land 
                    p+=4
                    #check if top neighbor is land, if yes, decrement 2 
                    for dr, dc in directions: 
                        nr= r+dr
                        nc=dc+c
                        if 0<=nr<m and 0<=nc<n and g[nr][nc]==1: 
                            p-=1
        return p
