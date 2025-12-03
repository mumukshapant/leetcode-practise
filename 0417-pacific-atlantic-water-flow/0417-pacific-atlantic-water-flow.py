class Solution(object):
    def pacificAtlantic(self, height):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m= len(height)
        n= len(height[0])
        
        directions= [[1,0],[0,1],[-1,0],[0,-1]]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevheight): 
            if ( r>=m or c>=n or r<0 or c<0 
            or (r,c) in visited 
            or height[r][c] <prevheight) : 
                return 

            visited.add((r,c))

            for d in directions: 
                newrow= d[0]+r
                newcol = d[1]+c
                dfs(newrow , newcol, visited, height[r][c])
        

        # 0th col poora pacific & 
        # last col poora atlantic 
        for r in range(m):
            dfs(r,0, pacific, height[r][0]) # 00, 10, 20 PAC
            dfs(r,n-1, atlantic, height[r][n-1]) #04, 14, 24 ATL
        
        # first row PAC 
        # last row ATL
        for c in range(n): 
            dfs(0,c , pacific, height[0][c]) #00 , 01, 02, 03, 04 PAC 
            dfs(m-1, c, atlantic, height[m-1][c]) # 20, 21, 22, 23, 24 ATL
        
        res=[]
        for r in range(m): 
            for c in range(n): 
                if (r,c) in pacific and (r,c) in atlantic: 
                    res.append([r,c])
        return res 




        