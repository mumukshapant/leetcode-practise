class Solution(object):
    def findCheapestPrice(self, n, nums, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        # Dijkstra's Algorithm

        adj = defaultdict(list)

        for u,v,w in nums: 
            adj[u].append((v,w))
        
        q=[(0,0,src)] # cost, stops, node
        vis={} 

        while q: 
            w1,stops, n1 = heapq.heappop(q)

            if n1 ==dst :
                return w1

            if stops>k:
                continue 
            
            if(n1, stops) in vis: 
                continue 
            
            vis[(n1,stops)]= w1
            
            for n2,w2 in adj[n1]: 
                if (n2, stops+1) not in vis: 
                    heapq.heappush(q, (w1+w2,stops+1, n2))
        return -1





        