class Solution(object):
    def numBusesToDestination(self, routes, s, t):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        
        # BFS -- because finding the shortest distance ( bfs on an undirected graph gives shortest possible path)
        if s==t: 
            return 0 

        adj= defaultdict(set)
        q = deque([(s,0)]) # source, number_of_bus_taken

        visited_bus = set() 
        visited_stop = set()

        for bus, route in enumerate(routes): 
              # 0, [1,2,7]
              for stop in route: 
                adj[stop].add(bus)
        
        while q: 
            currstop, route_len = q.popleft() 
            if currstop==t: 
                return route_len
            
            for nei_bus in adj[currstop]: 
                if nei_bus not in visited_bus: 
                    visited_bus.add(nei_bus)

                    for currstop in routes[nei_bus]:
                        if currstop not in visited_stop: 
                            visited_stop.add(currstop)
                            q.append((currstop, route_len+1))
        
        return -1 


            

        




