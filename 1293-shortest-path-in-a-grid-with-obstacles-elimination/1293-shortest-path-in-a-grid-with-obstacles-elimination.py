class Solution(object):
    def shortestPath(self, g, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m= len(g)
        n = len(g[0])

        t = (m-1,n-1)

        if k>=(m+n-2):
            return m+n-2

        directions = ((1,0),(0,1),(-1,0),(0,-1))
        q=deque() # no_steps, r,c, obstacles_left 
        q.append((0,0,0,k))

        seen= set((0,0,k)) # r,c, obstacles_left

        while q : 
            steps, r, c, obstacles_left= q.popleft()
            if (r,c)==t: 
                return steps
            
            for dr,dc in directions: 
                nr= dr+r
                nc = dc+c 

                if 0<=nr<m and 0<=nc<n: 
                    updated_remaining_obstacle = obstacles_left - g[nr][nc] # the obstacle is subtracted only when g[nr][nc] !=0, ie 1 , ie an obstacle because subtracting 0 doesn't make a difference. 

                    newstate = (nr, nc, updated_remaining_obstacle)

                    if updated_remaining_obstacle>=0 and newstate not in seen: 
                        seen.add(newstate)
                        q.append((steps+1 , nr, nc, updated_remaining_obstacle))
        return -1




