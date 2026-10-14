class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n=len(rooms)
        vis=set()

        def dfs(index): 
            if index not in vis: 
                vis.add(index)
            
            for key in rooms[index] : # index=0, key : [1,3]
            # if key is in visited, toh lock khul jayega so no need to do anything
                if key not in vis: 
                    dfs(key)
        dfs(0)

        return len(vis)==n

