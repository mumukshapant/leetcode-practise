class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Time complexity : O( n log n )
        pq = [] 

        for x,y in points: 
            dist = -(x*x + y*y ) 
            heapq.heappush(pq, [dist, x, y])
            if len(pq)>k :
                heapq.heappop(pq)
        
        res = [] 
        while pq :
            dist, x, y = heapq.heappop(pq)
            res.append([x,y])
        return res 
