class Solution(object):
    def shortestBridge(self, g):
    
        #  1) DFS helps us find all the cells belonging to the island1. 
            # basically to know EXACTLY which cells belong to island1.
            # This is important coz -- If we don't identify the first island, how do we know which cells we should start BFS from?
        # 2)  Find minimum distance bw island1 and island2 -- bfs 
        
        """
        DFS answers: Where is the first island?
        BFS answers: How many water cells away is the second island?
        """

        m, n = len(g), len(g[0])
        directions =[[1,0],[0,1],[0,-1],[-1,0]]
        
        # mark/ find first island 
        def dfs(i,j): 
            g[i][j]=2 #mark visited
            for dx, dy in directions: 
                nx, ny = dx+i, dy+j
            
                if 0<=nx<m and 0<=ny<n and g[nx][ny]==1: 
                    dfs(nx, ny)

        # fidning the island1 using DFS
        found=0 
        for i in range(n): 
            if found==1 : 
                break 
            for j in range(n) :
                if g[i][j]==1: 
                    dfs(i,j)
                    found=1 
                    break 
        
        
        # island is found, we used '2' as marker. 
        q = deque([(i,j,0) for i in range(n) for j in range(n) if g[i][j] == 2])
        
        # RUnning BFS now

        while  q: 
            cx, cy, dist = q.popleft() 
            for dx, dy in directions : 
                nx, ny = cx+dx , cy+dy
                if 0<= nx<n and 0<= ny < n and g[nx][ny] != 2:
                    if g[nx][ny]==1: 
                        return dist 
                    
                    g[nx][ny]=2
                    q.append((nx, ny, dist+1))
        return -1



