class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = len(piles)
        piles.sort()
        

        lo,hi = 1,max(piles)
        while lo<=hi : 
            time=0
            mid = lo+(hi-lo)//2
            for i in range(n): 
                time += math.ceil(piles[i] / float(mid))  
            if time>h : 
                lo= mid+1 
            else: 
                
                hi= mid-1
        
        return lo
        