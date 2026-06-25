from os import times
class TimeMap(object):

    def __init__(self):
        self.mapping = {} # key, value

    def set(self, key, val, time):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        
        if key not in self.mapping: 
            self.mapping[key] = [] #initialize a new list 
         
        self.mapping[key].append((time, val))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.mapping: 
            return ""
        values = self.mapping[key]
        res=""

        # binary search 
        lo,hi = 0, len(values)-1 
        while lo<=hi : 
            mid = lo+(hi-lo)//2
            if values[mid][0] <= timestamp: 
                res = values[mid][1]
                lo = mid+1 
            else: 
                hi = mid -1 
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)