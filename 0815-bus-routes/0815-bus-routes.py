class Solution(object):
    def numBusesToDestination(self, routes, s, t):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if s==t: 
            return 0

        adj= defaultdict(list)
        q= deque([(s,0)]) # source, number of bus taken 
        
        visited_bus= set()
        visited_stop = set() 

        for bus, route in enumerate(routes):  # enum turns to (index, element)  
            # 0,[1,2,7]
            # 1, [3,6,7]
            for stop in route: 
                adj[stop].append(bus)
        
        while q: 
            currstop , route_len = q.popleft() # 1 , 0 
            if currstop == t: 
                return route_len
            
            for nei_bus in adj[currstop]:  # currstop=1 , nei_bus = 0
                if nei_bus not in visited_bus: 
                    visited_bus.add(nei_bus)

                    for currstop in routes[nei_bus] : # currstop =1 in routes[0]
                        if currstop not in visited_stop : 
                            visited_stop.add(currstop)
                            q.append((currstop, route_len+1))
        
        return -1 


