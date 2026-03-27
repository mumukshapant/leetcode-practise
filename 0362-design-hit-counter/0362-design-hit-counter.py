class HitCounter(object):

    def __init__(self):
        self.q=[] 

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.q.append(timestamp)
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        t = timestamp - 299 
        lo = 0 
        hi = len(self.q) - 1
        
        while lo<=hi : 
            mid = lo+(hi-lo)//2
            if self.q[mid]>=t: 
                hi = mid-1
            else: 
                lo = mid+1 
        return len(self.q)-lo

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)