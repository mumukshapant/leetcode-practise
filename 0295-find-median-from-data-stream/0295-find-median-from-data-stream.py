class MedianFinder(object):

    def __init__(self):
        self.max_heap = [] # no max heap in PY so we add -ve values
        self.min_heap = [] 
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap,-num)
        
        largest_in_left = -heapq.heappop(self.max_heap)

        heapq.heappush(self.min_heap, largest_in_left)

        if len(self.min_heap) > len(self.max_heap):
            smallest_in_right = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_in_right)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            left_middle = -self.max_heap[0]
            right_middle = self.min_heap[0]
            return (left_middle + right_middle) / 2.0

        # Otherwise max_heap has one extra element,
        # and its top is the median
        return float(-self.max_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()